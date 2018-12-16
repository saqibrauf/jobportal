from django.shortcuts import render
from .models import Location, Category, Company, Job
from taggit.managers import TaggableManager


def home(request):
	"""
	try:
		location = request.session['CITY']
		location = Location.objects.get(name__iexact=location)
		all_jobs = Job.objects.filter(location__in=location.get_descendants(include_self=True)).distinct()
	except:
		all_jobs = Job.objects.all()
	"""
	all_jobs = Job.objects.all()	
	context = {
		'all_jobs' : all_jobs
	}
	return render(request, 'jobportal/home.html', context)

def job_detail(request, id, slug):
	job = Job.objects.get(id=id)
	context = {
		'job' : job,
	}
	return render(request, 'jobportal/job_detail.html', context)