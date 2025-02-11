from django.urls import path
from .views import upload_resume, resume_results

urlpatterns = [
    path('', upload_resume, name='upload_resume'),
    path('results/<int:resume_id>/', resume_results, name='resume_results')
]