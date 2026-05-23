# AI Resume Analyzer - Starter

def analyze_resume(text):
    print("Analyzing resume...")
    return {
        "skills_found": [],
        "recommendations": []
    }

if __name__ == "__main__":
    sample_text = "Sample resume content"
    result = analyze_resume(sample_text)
    print(result)
