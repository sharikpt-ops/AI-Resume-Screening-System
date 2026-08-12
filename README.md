# AI-Resume-Screening-System
AI-based system for automated resume screening and candidate matching

## 📌 Project Overview
This project automates the recruitment process using Artificial Intelligence by analyzing resumes and matching candidates with job descriptions.

## 🚀 Features
- Resume Parsing using NLP
- Skill Extraction
- Candidate Matching Algorithm
- Automated Scoring System

## 🛠️ Tech Stack
- Python
- Flask
- NLP (spaCy, NLTK)
- JSON

## ⚙️ Setup Instructions
1. Install dependencies:
   pip install -r requirements.txt

2. Run the application:
   python app.py

3. Test API using Postman:
   POST /match

## 📊 Sample Input

```json
{
  "name": "Abdul Sharik",
  "skills": ["Python", "SQL", "Machine Learning"],
  "experience": 2
}
```

## 📈 Output

```json
{
  "candidate_name": "Abdul Sharik",
  "match_score": 85.0
}
```

## 📸 Screenshots

### API Running
[API](screenshots/api_running.png)

### Open Browser
[Open Browser](screenshots/open_browser.png)

### Match Result
[Result](screenshots/output.png)
