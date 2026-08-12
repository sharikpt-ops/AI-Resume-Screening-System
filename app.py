from flask import Flask, request, jsonify
from matcher import calculate_match_score

app = Flask(__name__)

# Sample Job Description
job_description = {
    "skills": ["Python", "SQL", "Machine Learning"],
    "experience": 3
}

@app.route("/")
def home():
    return "AI Resume Screening System Running"

@app.route("/match", methods=["POST"])
def match_resume():
    candidate = request.json
    score = calculate_match_score(candidate, job_description)
    
    return jsonify({
        "candidate_name": candidate.get("name"),
        "match_score": score
    })

if __name__ == "__main__":
    app.run(debug=True)
