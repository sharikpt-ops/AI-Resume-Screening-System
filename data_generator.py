import random
import json

names = ["Abdul Sharik", "Mangesh Pande", "Nupursingh Shukla"]
skills_pool = ["Python", "Java", "SQL", "Machine Learning", "Data Analysis"]

def generate_resume():
    return {
        "name": random.choice(names),
        "skills": random.sample(skills_pool, 3),
        "experience": random.randint(1, 5),
        "education": "B.Tech / MCA / MBA"
    }

def generate_dataset(n=100):
    return [generate_resume() for _ in range(n)]

if __name__ == "__main__":
    resumes = generate_dataset(100)
    
    with open("sample_data/resumes.json", "w") as f:
        json.dump(resumes, f, indent=4)
    
    print("Sample resumes generated successfully!")
