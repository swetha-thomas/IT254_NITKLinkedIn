from django.db import models
from django.contrib.auth.models import User
# from login_logout.models import CustomUser

# Create your models here.

class Student(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  user_name = models.CharField(max_length=20, blank=False)
  first_name = models.CharField(max_length=50, blank=False)
  last_name = models.CharField(max_length=50)
  
  def __str__(self):
    return '{} : {}'.format(self.user_name, self.first_name)
  
  