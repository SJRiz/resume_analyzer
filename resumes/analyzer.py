import os
import fitz # This is PyMuPDF; used to extract texts from a PDF
import google.generativeai as genai # This will be used to read the resume and how well it matches the job description

from dotenv import load_dotenv

model = genai.GenerativeModel("gemini-pro")

# Get api key from the env (hidden)
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# This function will return the text from a pdf file as a string
def get_pdf_text(pdf_path):

    # Get the text from a pdf file
    doc = fitz.open(pdf_path)

    # Start with an empty string, and keep adding words from the pdf 
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# This function will get the resume text and job description, ask Gemini for a response, and return the responses as a string
def analyze_resume(resume_text, job_desc):

    # Ask Gemini to compare the resume with the job description, and give a numerical score
    feedback_prompt = f"See how well this resume:\n\n({resume_text})\n\n Matches with this job description:\n\n({job_desc})\n\n and give feedback. Make the feedback 2-3 coherent paragraph(s) and between each paragraph type backwardslash n (basically the newline command in python), and dont use bold or headers. If you use multiple paragraphs, ensure there is at least 2 spaces between them. If the resume does not look like a resume or if the job description does not look like a proper job description, only respond with 'Cannot give feedback because the resume and/or the job description does not seem valid' "
    score_prompt = f"now only respond with a single numerical score from 0 to 100 to compare how well this resume:\n\n({resume_text})\n\n Matches with this job description:\n\n({job_desc})\n\n If the resume and/or the job description does not look like a valid job description or resume automatically respond with a 0. If the resume is valid, but the job description is not, respond with 0"
    feedback_response = model.generate_content(feedback_prompt)
    score_response = model.generate_content(score_prompt)

    return feedback_response.text, score_response.text

