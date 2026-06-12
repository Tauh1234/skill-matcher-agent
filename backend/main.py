from fastapi import FastAPI
from pydantic import BaseModel
from matcher import extract_skills, match_percentage

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Skill Matcher API Running Successfully"}

class MatchRequest(BaseModel):
    resume_text: str
    job_description: str

@app.post("/match")
def match(req: MatchRequest):
    resume_skills = extract_skills(req.resume_text)
    jd_skills = extract_skills(req.job_description)

    percentage = match_percentage(
        resume_skills,
        jd_skills
    )

    return {
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "match_percentage": percentage
    }