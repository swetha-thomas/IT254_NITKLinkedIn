from django.db import models
from organization.models import Organization 


# Create your models here.

class Job(models.Model):
  job_name = models.CharField(max_length=150)
  company = models.ForeignKey(Organization, on_delete=models.CASCADE)
  location_of_work = models.CharField(max_length=200)
  job_type = models.CharField(max_length=9)
  job_level = models.CharField(max_length=100)
  site_url = models.CharField(max_length=300)
  job_description = models.TextField()