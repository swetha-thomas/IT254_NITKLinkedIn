from django.contrib import admin
from .models import Student, WorkExperience

# Register your models here.

class StudentModelAdminConfig(admin.ModelAdmin):
  search_fields = ('username', 'first_name', 'last_name')
  ordering = ('first_name', 'year_of_pass_out')
  list_display = ('username', 'first_name', 'last_name','year_of_pass_out', 'profile_pic')
 
  fieldsets = (
    (None, {'fields': ('user', 'first_name', 'last_name', 'gender', 'dob', 'roll_no', 'branch', 'semester', 'cgpa', 'contact', 'year_of_pass_out', 'aboutme' 'profile_pic')}),
  )
  
  add_fieldsets = (
    (None, {
      'classes' : ('wide',),
      'fields' : ('user', 'first_name', 'last_name', 'gender', 'dob', 'roll_no', 'branch', 'semester', 'cgpa', 'contact', 'year_of_pass_out', 'aboutme' 'profile_pic'),
      }),
  )


admin.site.register(Student, StudentModelAdminConfig)
