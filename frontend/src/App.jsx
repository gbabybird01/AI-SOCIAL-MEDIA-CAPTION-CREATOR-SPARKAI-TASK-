import { useState } from "react";
import "./App.css";

function App() {
  const [brief, setBrief] = useState("");
  const [platform, setPlatform] = useState("instagram");
  const [tone, setTone] = useState("friendly");
  const [imageFile, setImageFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:5001";

  const handleSubmit = async (e) => {
  e.preventDefault();
  setLoading(true);
  setError(null);

  try {
    const response = await fetch(`${API_URL}/generate`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json", 
      },
      body: JSON.stringify({
        brief: brief,       
        platform: "instagram",
        tone: "friendly",
        audience: "general",
      }),
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const data = await response.json();
    setResult(data);
  } catch (err) {
    console.error("Fetch failed:", err);
    setError("Failed to fetch captions. Please try again.");
  } finally {
    setLoading(false);
  }
};


  function handleFileChange(e) {
    const f = e.target.files[0];
    setImageFile(f || null);
  }

  return (
    <div className="container">
      <h1>Spark AI Social Media Caption Creator</h1>
      <h2>Create social media captions for your business posts in just one click using the power of AI!</h2>

      <form onSubmit={handleSubmit}>
        <div className="input-row">
          <div className="input-block">
            <label><strong>Upload an Image:</strong></label>
            <input type="file" accept="image/*" onChange={handleFileChange} />
          </div>

          <span className="or-text">OR</span>


          <div className="input-block">
            <label><strong>Enter a Text Brief:</strong></label>
            <textarea
              value={brief}
              onChange={(e) => setBrief(e.target.value)}
              placeholder="Describe your product or post idea..."
            />
          </div>
        </div>

        <div className="row">
          <label>
            Select Platform:
            <select value={platform} onChange={(e) => setPlatform(e.target.value)}>
              <option>Instagram</option>
              <option>Twitter</option>
              <option>Linkedin</option>
            </select>
          </label>

          <label>
            Set Tone:
            <select value={tone} onChange={(e) => setTone(e.target.value)}>
              <option>Friendly</option>
              <option>Professional</option>
              <option>Playful</option>
            </select>
          </label>

          <button type="submit" disabled={loading}>
            {loading ? "Generating..." : "Generate"}
          </button>
        </div>
      </form>

      {error && <p className="error">{error}</p>}

      {result && (
        <div className="results">
          <h3>Generated Captions</h3>
          {result.captions.map((c, i) => (
            <div key={i} className="card">
              <p><strong>Caption {i + 1}:</strong> {c.text}</p>
              <p className="hashtags">{c.hashtags.join(" ")}</p>
            </div>
          ))}
          <div className="card">
            <strong>Suggested Time:</strong> {result.suggested_time}
            <p>{result.rationale}</p>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;

