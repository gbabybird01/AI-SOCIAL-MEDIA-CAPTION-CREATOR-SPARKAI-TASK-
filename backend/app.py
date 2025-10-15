
import os
import json
import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("Set OPENAI_API_KEY in your environment or .env file")

openai.api_key = OPENAI_API_KEY


app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})

#prompt template 
PROMPT_TEMPLATE = """
You are a creative social media caption writer.
INPUT: {seed_text}
Platform: {platform}
Tone: {tone}
Audience: {audience}

TASK:
1) Produce exactly 3 short captions tailored to the Platform and Tone.
2) For each caption, provide 3 relevant hashtags as a JSON array.
3) Suggest one best posting time (ISO 8601 format) and a one-sentence rationale.
4) Output ONLY valid JSON in this exact format:

{{
  "captions": [
    {{"text":"...","hashtags":["#...","#...","#..."]}},
    {{"text":"...","hashtags":["#...","#...","#..."]}},
    {{"text":"...","hashtags":["#...","#...","#..."]}}
  ],
  "suggested_time":"YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
  "rationale":"one-sentence rationale"
}}
"""

def build_prompt(seed_text, platform="instagram", tone="friendly", audience="general"):
    return PROMPT_TEMPLATE.format(
        seed_text=seed_text.strip(),
        platform=platform,
        tone=tone,
        audience=audience,
    )

#Chat Completion LLM
def call_llm(prompt):

    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=500,
    )
    return resp["choices"][0]["message"]["content"]


@app.route("/generate", methods=["POST", "OPTIONS"])
def generate():

    if request.method == "OPTIONS":
        return jsonify({"message": "CORS preflight OK"}), 200

    print("Received POST /generate")
    print("Headers:", dict(request.headers))

    # parsing JSON 
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON body"}), 400

    if not data or "brief" not in data:
        return jsonify({"error": "Missing 'brief'"}), 400

    brief = data["brief"]
    platform = data.get("platform", "instagram")
    tone = data.get("tone", "friendly")
    audience = data.get("audience", "general")


    prompt = build_prompt(brief, platform, tone, audience)

    try:
        llm_output = call_llm(prompt)
    except Exception as e:
        print("LLM call failed:", e)
    
        return jsonify({
            "captions": [
                {"text": "Sample caption 1", "hashtags": ["#test", "#demo"]},
                {"text": "Sample caption 2", "hashtags": ["#test2", "#demo2"]},
                {"text": "Sample caption 3", "hashtags": ["#test3", "#demo3"]}
            ],
            "suggested_time": "2025-10-14T21:30:00+00:00",
            "rationale": "Test data returned due to LLM failure."
        })


    try:
        parsed = json.loads(llm_output)
    except Exception:
        match = re.search(r"\{(?:.|\n)*\}", llm_output)
        if match:
            try:
                parsed = json.loads(match.group(0))
            except Exception:
                return jsonify({"error": "Invalid JSON in model output", "model_output": llm_output}), 500
        else:
            return jsonify({"error": "Model did not return JSON", "model_output": llm_output}), 500


    if "captions" not in parsed:
        return jsonify({"error": "Missing 'captions' field", "parsed": parsed}), 500

    return jsonify(parsed)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
