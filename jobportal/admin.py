from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from jobportal.models import Location, Category, Company, Job


class LocationAdmin(MPTTModelAdmin):
	autocomplete_fields = ['parent']
	search_fields = ['name']

class CategoryAdmin(MPTTModelAdmin):
	autocomplete_fields = ['parent']
	search_fields = ['name']

class CompanyAdmin(admin.ModelAdmin):
	exclude = ['user']
	autocomplete_fields = ['location', 'category']
	search_fields = ['name']

	def locations(self, obj):
		data = obj.location.all()
		locations = list()
		for d in data:
			locations.append(d.name)
		return locations

	list_display = ['name', 'slug', 'website', 'locations', 'user']

class JobAdmin(admin.ModelAdmin):
	autocomplete_fields = ['location', 'category', 'company', 'tags']
	search_fields = ['title']
	radio_fields = {'gender': admin.HORIZONTAL}
	exclude = ['job_url']
	list_display = ['created_at', 'title', 'slug', 'company', 'location', 'category']


admin.site.register(Location, LocationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Job, JobAdmin)

