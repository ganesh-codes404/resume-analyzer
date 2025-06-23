import fitz 
import argparse

KEY_SKILLS = ["Python", "SQL", "Machine Learning", "Data Science", "Deep Learning", "AWS", "Git"]

# PDF Text
def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# keyword counter
def analyze_text(text):
    text_lower = text.lower()
    skill_counts = {}
    for skill in KEY_SKILLS:
        count = text_lower.count(skill.lower())
        skill_counts[skill] = count
    return skill_counts

# suggestions function
def suggest_improvements(skill_counts):
    missing_skills = [skill for skill, count in skill_counts.items() if count == 0]
    if missing_skills:
        print("\n Suggested Improvements:")
        print(f"Consider adding: {', '.join(missing_skills)}")
    else:
        print("\n Great! All key skills are present.")

# CLI setup similar to the other CLI question
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resume Analyzer Tool")
    parser.add_argument("pdf_path", help="Path to the resume PDF")

    args = parser.parse_args()

    print(f"\n Analyzing: {args.pdf_path}\n")
    resume_text = extract_text(args.pdf_path)
    skills = analyze_text(resume_text)

    print(" Skill Mentions:")
    for skill, count in skills.items():
        print(f"{skill}: {count}")

    suggest_improvements(skills)
