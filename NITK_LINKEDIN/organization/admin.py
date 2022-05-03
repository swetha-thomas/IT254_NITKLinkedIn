from django.contrib import admin

from organization.models import Organization

# Register your models here.

# just basic adminConfig so that i can continue w jobs
class OrganizationModelAdminConfig(admin.ModelAdmin):
  search_fields = ('org_name', 'user')
  ordering = ('org_name','user')
  list_display = ('user', 'org_name',)
 
  fieldsets = (
    (None, {'fields': ('user', 'org_name')}),
  )
  
  add_fieldsets = (
    (None, {
      'classes' : ('wide',),
      'fields' : ('user', 'org_name',),
      }),
  )

admin.site.register(Organization, OrganizationModelAdminConfig)
