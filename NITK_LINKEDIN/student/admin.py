from django.contrib import admin
from .models import Student

# Register your models here.

class StudentModelAdminConfig(admin.ModelAdmin):
  search_fields = ('username', 'first_name', 'branch',)
  ordering = ('first_name', 'year_of_pass_out')
  list_display = ('username', 'first_name', 'branch', 'year_of_pass_out', 'profile_pic',)
 
  fieldsets = (
    (None, {'fields': ('user', 'first_name', 'last_name', 'semester', 'branch', 'cgpa', 'year_of_pass_out', 'profile_pic')}),
  )
  
  add_fieldsets = (
    (None, {
      'classes' : ('wide',),
      'fields' : ('user', 'first_name', 'last_name', 'semester', 'branch', 'cgpa', 'year_of_pass_out', 'profile_pic'),
      }),
  )

admin.site.register(Student, StudentModelAdminConfig)