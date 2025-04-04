from django.db import models

# Create your models here.

class Resume(models.Model):
    # Name, file and job description will be filled out by the form
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='resumes/PDFs/')
    job_description = models.TextField()

    # Score and feedback will be filled through DeepSeek's AI
    score = models.FloatField(null=True, blank=True)
    feedback = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    # The resume data will be seen as the name in the database
    def __str__(self):
        return self.name