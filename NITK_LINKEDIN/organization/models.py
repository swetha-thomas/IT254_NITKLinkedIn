from django.db import models

# Create your models here.

# just basic model so that i can continue w jobs
class Organization(models.Model):
  org_name = models.CharField(max_length=500)
  
  def __str__(self):
    return self.org_name