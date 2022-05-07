from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

import datetime

# Create your models here.

class Student(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  first_name = models.CharField(max_length=50, blank=False, default="")
  last_name = models.CharField(max_length=50, null=True,  default="")
  gender = models.CharField(max_length=6, null=False, blank=True,  default="other")
  dob = models.DateField(null=True, blank=True, auto_now_add=False, default=datetime.date.today)
  roll_no = models.CharField(max_length=12, null=True, default="")
  branch = models.CharField(max_length=50, null=True, default="")
  semester = models.IntegerField(blank=True, null=True, default=1)
  cgpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True, default=0.0)
  contact = models.CharField(max_length=15, default="+910000000000")
  year_of_pass_out = models.IntegerField(blank=True, null=True, default=2022)
  aboutme = models.TextField(max_length=15, blank=True, null=True)
  profile_pic = models.ImageField(upload_to='student_profile_uploads/', blank=True, default="default_student_profile.jpeg")
  
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
      4: 'th',
      5: 'th',
      6: 'th',
      7: 'th',
      8: 'th',
    }
    return matcher.get(self.semester, '')
    
  def __str__(self):
    return '{} : {}  {}'.format(self.username, self.first_name, self.last_name)

class WorkExperience(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  role = models.CharField(max_length=50, blank=False)
  company = models.CharField(max_length=50, blank=False)
  location = models.CharField(max_length=50, blank=False)
  employment_type = models.CharField(max_length=50, blank=False)
  start_date = models.CharField(max_length=50,blank=False)
  end_date = models.CharField(max_length=50)

class Clubs(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  role = models.CharField(max_length=50, blank=False)
  club_name = models.CharField(max_length=100, blank=False)
  start_date = models.CharField(max_length=50,blank=False)
  end_date = models.CharField(max_length=50)

class Skills(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  skill = models.CharField(max_length=100, blank=False)

class Education(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  institute = models.CharField(max_length=100, blank=False)
  degree = models.CharField(max_length=100, blank=False)
  start_date = models.CharField(max_length=50,blank=False)
  end_date = models.CharField(max_length=50)

class Courses(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  course_name = models.CharField(max_length=100, blank=False)
  organization = models.CharField(max_length=100, blank=False)
  start_date = models.CharField(max_length=50,blank=False)
  end_date = models.CharField(max_length=50)
  