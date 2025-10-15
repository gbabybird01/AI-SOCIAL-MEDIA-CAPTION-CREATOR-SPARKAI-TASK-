AI-SOCIAL-MEDIA-CAPTION-CREATOR-SPARKAI-TASK 

##DISCLAIMER
This project was developed as a task assigned for an interview. 

**SAMPLE IMAGES ARE UNDER THE use_cases FOLDER**
--

##OVERVIEW
This is a web app that generates 3 creative social media captions and 3 relevant hashtags from the image (A.K.A. the post) or text brief of the post uploaded, the platform that the post is being uploaded to and the tone that is aimed to set.

--
#THE UI IN ACTION 

![alt text](use_cases\image-2.png)

-USE CASE : TEXT BRIEF (A teddy bear product that calms children down with music when crying)
 ->CASE 1 : PLATFORM- INSTAGRAM 
    ~USE CASE 1.1 : TONE : FRIENDLY
        ![alt text](use_cases\image-3.png)
    ~USE CASE 1.2 : TONE : PLAYFUL
        ![alt text](use_cases\image-4.png)
    ~USE CASE 1.3 : TONE : PROFESSIONAL
        ![alt text](use_cases\image-5.png)

 ->CASE 2 : PLATFORM- LINKEDIN 
    ~USE CASE 2.1 : TONE : FRIENDLY
        ![alt text](use_cases\image-7.png)
    ~USE CASE 2.2 : TONE : PLAYFUL
        ![alt text](use_cases\image-8.png)
    ~USE CASE 2.3 : TONE : PROFESSIONAL
        ![alt text](use_cases\image-6.png)

 ->CASE 3 : PLATFORM- TWITTER
    ~USE CASE 3.1 : TONE : FRIENDLY
        ![alt text](use_cases\image-10.png)
    ~USE CASE 3.2 : TONE : PLAYFUL
        ![alt text](use_cases\image-9.png)
    ~USE CASE 3.3 : TONE : PROFESSIONAL
        ![alt text](use_cases\image-11.png)

-USE CASE : IMAGE (a coffee cup)
![alt text](use_cases\image-12.png)
 

#PROMPT DESIGN : 

The following was the prompt used : 
    "" You are a creative social media caption writer.
    INPUT: {seed_text}
    Platform: {platform}
    Tone: {tone}
    Audience: {audience}

    TASK:
    1. Produce exactly 3 short captions tailored to the Platform and Tone.
    2. For each caption, provide 3 relevant hashtags as a JSON array.
    3. Suggest one best posting time (ISO 8601 format) and a one-sentence rationale.
    4. Output ONLY valid JSON in this exact format:

    {{
    "captions": [
        {{"text":"...","hashtags":["#...","#...","#..."]}},
        {{"text":"...","hashtags":["#...","#...","#..."]}},
        {{"text":"...","hashtags":["#...","#...","#..."]}}
    ],
    "suggested_time":"YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
    "rationale":"one-sentence rationale"
    }}
    ""

--

#CHALLENGES


During the project the challenge I faced was to build the LLM integration as I have not worked with LLMs before and had to learn to use LLM APIs in a day. Due to this as you can run and see, the image upload and then captioning does not give desired results at all times.







"# AI-SOCIAL-MEDIA-CAPTION-CREATOR-SPARKAI-TASK-" 
