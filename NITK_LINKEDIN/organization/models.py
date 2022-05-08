from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

# Create your models here.

class Organization(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  org_name = models.CharField(max_length=100, null=True, blank=True, default="")
  industry = models.CharField(max_length=50, null=True, blank=True, default="")
  company_size = models.CharField(max_length=50, null=True, blank=True, default="")
  company_type = models.CharField(max_length=50, null=True, blank=True, default="")
  locations = models.CharField(max_length= 200, null=True, blank=True, default="")
  website_url = models.CharField(max_length= 100, null=True, blank=True, default="")
  contact_no = models.CharField(max_length= 20, null=True, blank=True, default="")
  company_desc = models.CharField(max_length= 200, null=True, blank=True, default="")
  num_alumni = models.IntegerField(null=True, blank=True, default=0)
  profile_pic = models.ImageField(upload_to='org_profile_uploads/', null=True, blank=True, default="org_profile_uploads/default_org_profile.png")

  def __str__(self):
    return self.org_name

  def image_tag(self):
    return mark_safe('<img src="%s" width="50" height="50" />' % (self.profile_pic))
  
  # def __str__(self):
  #   return '{} : {}'.format(self.org_name, self.locations)