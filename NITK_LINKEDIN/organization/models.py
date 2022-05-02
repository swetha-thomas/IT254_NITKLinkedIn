from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

# Create your models here.

class Organization(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  org_name = models.CharField(max_length=100, blank=False)
  email = models.EmailField(max_length=100)
  industry = models.CharField(max_length=50)
  company_size = models.CharField(max_length=50)
  company_type = models.CharField(max_length=50)
  locations = models.CharField(max_length= 200, blank=False)
  website_url = models.CharField(max_length= 100)
  contact_no = models.CharField(max_length= 20, blank=False)
  company_desc = models.CharField(max_length= 200)
  profile_pic = models.ImageField(upload_to='org_profile_uploads/', blank=True, default="default_org_profile.jpeg")

  def __str__(self):
    return self.org_name

  def image_tag(self):
    return mark_safe('<img src="%s" width="50" height="50" />' % (self.profile_pic))
  
  def __str__(self):
    return '{} : {}'.format(self.org_name, self.locations)