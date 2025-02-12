import os
import fitz # This is PyMuPDF; used to extract texts from a PDF
import google.generativeai as genai # Alternative AI just in case
from openai import OpenAI # This will be used to read the resume and how well it matches the job description

from dotenv import load_dotenv

# Get api key from the env (hidden)
load_dotenv()

#model = genai.GenerativeModel("gemini-pro")
#genai.configure(api_key=os.getenv('GOOGLE_API_KEY')) -- Currently not in use, deepseek clears

client = OpenAI(api_key=os.getenv('OPENROUTER_API_KEY'),
                base_url = "https://openrouter.ai/api/v1")


# This function will return the text from a pdf file as a string
def get_pdf_text(pdf_path):

    # Get the text from a pdf file
    doc = fitz.open(pdf_path)

    # Start with an empty string, and keep adding words from the pdf 
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# This function will get the resume text and job description, ask DeepSeek for a response, and return the responses as a string
def analyze_resume(resume_text, job_desc):

    # Ask DeepSeek to compare the resume with the job description, and give a numerical score
    feedback_prompt = f"Act like an employer. Only use text. See how well this resume which is pasted between these quadruple brackets:\n\n(((({resume_text}))))\n\n Matches with this job description which is placed between these quadruple brackets:\n\n(((({job_desc}))))\n\n and give feedback. Make the feedback 2-3 coherent paragraph(s), and dont use bold or headers. Try to stay under 1000 characters. If you use multiple paragraphs, ensure there is at least 2 spaces between them. Respond with 'Cannot give feedback because the resume and/or the job description does not seem valid' if the resume is not a resume, or if the job description is not proper. "
    score_prompt = f"Think like an employer. Only respond with a single numerical score from 0 to 100 to compare how well this resume which is between these quadruple brackets:\n\n(((({resume_text}))))\n\n Matches with this job description which is between these quadruple brackets:\n\n(((({job_desc}))))\n\n. Think about which skills are transferrable too. Automatically give a 0 if necessary (ex. if resume is not valid or job description is improper)"
    summary_prompt = f"Briefly explain what the company wants, what the company is about, and what the job is about for this job description. Only use text and no bold or headers: {job_desc}"

    feedback_response = client.chat.completions.create(
        extra_body={},
        model = "deepseek/deepseek-chat:free",
        messages=[
            {
                "role": "user",
                "content": feedback_prompt
            }
        ]

    )
    score_response = client.chat.completions.create(
        extra_body={},
        model = "deepseek/deepseek-chat:free",
        messages=[
            {
                "role": "user",
                "content": score_prompt
            }
        ]

    )
    summary_response = client.chat.completions.create(
        extra_body={},
        model = "deepseek/deepseek-chat:free",
        messages=[
            {
                "role": "user",
                "content": summary_prompt
            }
        ]

    )

    return feedback_response.choices[0].message.content, score_response.choices[0].message.content, summary_response.choices[0].message.content

