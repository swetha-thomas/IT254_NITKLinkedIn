from django.contrib import admin
from .models import Student

# Register your models here.

class StudentModelAdminConfig(admin.ModelAdmin):
  search_fields = ('user_name', 'first_name', 'last_name',)
  ordering = ('user_name',)
  list_display = ('user_name', 'first_name', 'last_name',)
 
  fieldsets = (
    (None, {'fields': ('user', 'user_name', 'first_name', 'last_name')}),
  )
  
  add_fieldsets = (
    (None, {
      'classes' : ('wide',),
      'fields' : ('user', 'user_name', 'first_name', 'last_name',),
      }),
  )

admin.site.register(Student, StudentModelAdminConfig)