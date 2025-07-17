# 🧠 AI-Powered Resume Analyzer

A web app to extract, analyze, and score resumes using Natural Language Processing (NLP).

## 🔍 Features
- Upload a resume (PDF)
- Extract text and identify key entities (skills, education, experience)
- Compare against a job description
- Get a matching score and missing keyword suggestions

## 🚀 How to Run

```bash
git clone https://github.com/DheerajReddyE/resume-analyzer.git
cd resume-analyzer
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run main.py
