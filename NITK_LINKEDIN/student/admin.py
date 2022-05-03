from django.contrib import admin
from .models import Student

# Register your models here.

class StudentModelAdminConfig(admin.ModelAdmin):
  search_fields = ('username', 'first_name', 'last_name',)
  ordering = ('first_name',)
  list_display = ('username', 'first_name', 'last_name', 'image_tag')
 
  fieldsets = (
    (None, {'fields': ('user', 'first_name', 'last_name', 'semester', 'branch', 'cgpa', 'profile_pic')}),
  )
  
  add_fieldsets = (
    (None, {
      'classes' : ('wide',),
      'fields' : ('user', 'first_name', 'last_name', 'semester', 'branch', 'cgpa', 'profile_pic'),
      }),
  )

admin.site.register(Student, StudentModelAdminConfig)