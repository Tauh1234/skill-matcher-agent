import re
from skills import skills_db

def extract_skills(text):
    text = text.lower()

    found = []

    for skill in skills_db:
        if re.search(r'\b' + re.escape(skill) + r'\b', text):
            found.append(skill)

    return found


def match_percentage(resume_skills, jd_skills):

    matched = set(resume_skills) & set(jd_skills)

    if len(jd_skills) == 0:
        return 0

    return round((len(matched) / len(jd_skills)) * 100, 2)