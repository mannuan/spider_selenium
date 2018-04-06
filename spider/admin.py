from django.contrib import admin

# Register your models here.
from .models import Project, Website, Region, Type

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_id', 'name', 'status', 'website', 'region', 'type', 'created_time', 'modified_time', 'editor']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Website)
admin.site.register(Region)
admin.site.register(Type)
