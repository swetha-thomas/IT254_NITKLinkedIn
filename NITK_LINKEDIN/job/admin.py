from django.contrib import admin
from .models import Job

# Register your models here.

class JobModelAdminConfig(admin.ModelAdmin):
  search_fields = ('job_name', 'company', 'job_type',)
  ordering = ('job_name',)
  list_display = ('job_name', 'company', 'job_type', 'job_level', 'site_url')
 
  fieldsets = (
    (None, {'fields': ('job_name', 'company')}),
    ('Job Specifics', {'fields': ('job_type', 'job_level')}),
    ('Job Details', {'fields': ('location_of_work', 'site_url', 'job_description')}),
  )
  
  add_fieldsets = (
    (None, {
      'classes' : ('wide',),
      'fields' : ('job_name', 'company', 'location_of_work', 'job_type', 'job_level', 'site_url', 'job_description'),
      }),
  )

admin.site.register(Job, JobModelAdminConfig)
