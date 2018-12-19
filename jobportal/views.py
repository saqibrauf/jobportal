from django.shortcuts import render
from django.http import HttpResponse
from .models import Location, Category, Company, Job
from taggit.managers import TaggableManager
from django.views.decorators.csrf import csrf_exempt


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

@csrf_exempt
def job_posting(request):
	if request.method == 'POST':
		company = request.POST.get('company')
		city = request.POST.get('city')
		joburl = request.POST.get('joburl')
		job_name = request.POST.get('job_name')
		desc = request.POST.get('desc')

	#Check If Company Exists
	try:
		check_company=Company.objects.get(name__iexact=company)
		company_id = check_company.id
	except:
		new_company = Company.objects.create(name=company)
		new_company.save()
		check_company=Company.objects.get(name__iexact=company)
		company_id = check_company.id

	#Check If City Exists
	try:
		check_city=Location.objects.get(name__iexact=city)
		city_id = check_city.id		
	except:
		return HttpResponse('City Not Exists')

	#Check If Job Already Exists
	try:
		check_job = Job.objects.get(job_url__iexact=joburl)
		return HttpResponse('Job exists')
	except:
		add_new_job = Job.objects.create(title=job_name, desc=desc, company=Company.objects.get(id=company_id), location=Location.objects.get(id=city_id), job_url=joburl)
		add_new_job.save()

		return HttpResponse('Job added')