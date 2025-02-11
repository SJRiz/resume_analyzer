from django import forms
from .models import Resume

class ResumeUploadForm(forms.ModelForm):

    # The form model will be connected to the resume model
    class Meta:
        model = Resume

        # It will only take the name, job description to match, and file of the resume
        fields = ['name', 'file', 'job_description']
