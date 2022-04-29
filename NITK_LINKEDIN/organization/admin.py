from django.contrib import admin

from organization.models import Organization

# Register your models here.

# just basic adminConfig so that i can continue w jobs
class OrganizationModelAdminConfig(admin.ModelAdmin):
  search_fields = ('org_name', )
  ordering = ('org_name',)
  list_display = ('org_name',)
 
  fieldsets = (
    (None, {'fields': ('org_name', )}),
  )
  
  add_fieldsets = (
    (None, {
      'classes' : ('wide',),
      'fields' : ('org_name',),
      }),
  )

admin.site.register(Organization, OrganizationModelAdminConfig)
