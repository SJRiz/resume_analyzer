from django.shortcuts import render, redirect, HttpResponse
from .models import Resume
from .forms import ResumeUploadForm
from .analyzer import get_pdf_text, analyze_resume

# Create your views here.

# Default page. If the user submits a resume and job description, they will be redirected to the results page
def upload_resume(request):
    form = ResumeUploadForm(request.POST, request.FILES, request.POST)

    # If they filled out the required fields then get ready to analyze
    if form.is_valid():
        print("user submitted")

        # Save name and file to database
        resume = form.save()
        text = get_pdf_text(resume.file.path)
        feedback, score = analyze_resume(text, resume.job_description)
        print(feedback, score)

        # Save ai responses to database
        resume.score = score
        resume.feedback = feedback
        resume.save()

        # Send them to the results page, which will have their unique resume ID
        return redirect('resume_results', resume_id=resume.id)
    
    # This will be called if the user just visited the page
    else:
        print("user visited")
        form = ResumeUploadForm()
        return render(request, 'upload.html', {'form': form})
        

# Results page. They can also click "upload another resume" to go back to the upload page
def resume_results(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    resume.file.delete()
    return render(request, 'results.html', {'resume': resume})