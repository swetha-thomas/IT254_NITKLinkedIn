from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserAdminConfig(UserAdmin):
  search_fields = ('email',)
  ordering = ('-start_date',)
  list_display = ('email', 'is_staff', 'is_active', 'is_superuser', 'start_date')
  
  fieldsets = (
    (None, {'fields': ('email', 'is_student', 'is_organization')}),
    ('Permissions', {'fields': ('is_superuser', 'is_active')}),
    ('Personal', {'fields': ('start_date',)}),
  )
  
  add_fieldsets = (
    (None, {
      'classes' : ('wide',),
      'fields' : ('email', 'is_student', 'is_organization', 'is_superuser', 'is_active', ),
      }),
  )

admin.site.register(CustomUser, UserAdminConfig)