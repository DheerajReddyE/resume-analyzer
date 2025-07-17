import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    skills = []
    education = []
    experience = []

    for ent in doc.ents:
        if ent.label_ == "ORG" and "university" in ent.text.lower():
            education.append(ent.text)
        elif ent.label_ in ["DATE", "TIME"]:
            experience.append(ent.text)
        elif ent.label_ in ["PERSON", "GPE", "ORG", "PRODUCT"]:
            skills.append(ent.text)

    return {
        "skills": list(set(skills)),
        "education": list(set(education)),
        "experience": list(set(experience))
    }

def compute_score(resume_text, job_text):
    if not job_text.strip():
        return 0, []

    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, job_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    score_percent = round(score * 100, 2)

    resume_tokens = set(resume_text.lower().split())
    job_tokens = set(job_text.lower().split())
    missing_keywords = list(job_tokens - resume_tokens)

    return score_percent, missing_keywords[:10]

def analyze_resume(resume_text, job_description):
    entities = extract_entities(resume_text)
    score, missing = compute_score(resume_text, job_description)

    return {
        "entities": entities,
        "score": score,
        "missing_keywords": missing
    }
