from django.contrib import admin
from .models import Student
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class StudentAdminConfig(UserAdmin):
  search_fields = ('username', 'first_name', 'last_name',)
  ordering = ('-start_date', 'username',)
  list_display = ('username', 'first_name', 'last_name',)
 
  fieldsets = (
    (None, {'fields': ('username', 'first_name', 'last_name')}),
  )
  
  add_fieldsets = (
    (None, {
      'classes' : ('wide',),
      'fields' : ('username', 'first_name', 'last_name',),
      }),
  )

# admin.site.register(Student, StudentAdminConfig)
admin.site.register(Student)