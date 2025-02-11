This project allows users to upload a resume and paste a job description to get feedback and a score.
It utilizes Django for the backend, and HTML/Javascript for the frontend (the frontend is currently very basic, will be improving it later after brushing up on some skills)
This project also uses Google Gemini's free API to analyze the resume and the job description (API key is hidden).
PDFs and doc files are supported. PyMuPDF is used to extract texts from a pdf into a string for the code to use

Resumes and job descriptions submitted are stored in a database;
I am planning on implementing a feature that will use these for something, but for now it is only used for testing purposes to experiment with the django admin panel.
I am also working on more features such as a login system, and a way to select resumes you have already uploaded through the login system.
