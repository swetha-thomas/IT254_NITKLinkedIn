from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

# Create your models here.

class Student(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  first_name = models.CharField(max_length=50, blank=False)
  last_name = models.CharField(max_length=50, null=True)
  semester = models.IntegerField(blank=True, null=True)
  cgpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
  profile_pic = models.ImageField(upload_to='student_profile_uploads', blank=True, default="default_student_profile.jpeg")
  
  
  def image_tag(self):
    return mark_safe('<img src="%s" width="50" height="50" />' % (self.profile_pic))
  
  @property
  def username(self):
    return self.user.username
    
  @property
  def semesterSuffix(self):
    matcher = {
      1: "st",
      2: "nd",
      3: "rd",
    }
    return matcher.get(self.semester, 'th')
    
  def __str__(self):
    return '{} : {}  {}'.format(self.username, self.first_name, self.last_name)