from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('assigned_users', 'assigned_groups')

admin.site.register(Project, ProjectAdmin)
