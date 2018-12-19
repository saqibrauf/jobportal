from django.urls import path
from . import views

#app_name = 'jobportal'
urlpatterns = [
    path('', views.home, name='home'),
    path('job/<id>/<slug>', views.job_detail, name='job_detail'),
    path('job-posting', views.job_posting, name='job_posting'),
]