def calculate_match_score(candidate, job_description):
    # Skill matching
    skill_match = len(set(candidate["skills"]).intersection(set(job_description["skills"])))
    total_skills = len(job_description["skills"])
    
    skill_score = (skill_match / total_skills) * 100 if total_skills else 0

    # Experience matching
    experience_score = min(candidate["experience"] / job_description["experience"], 1) * 100

    # Final weighted score
    final_score = (0.7 * skill_score) + (0.3 * experience_score)
    
    return round(final_score, 2)
