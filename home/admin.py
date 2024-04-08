from django.contrib import admin
from .models import Project, Contact, Portfolio

# Register your models here.


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['user', 'resume']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_desc', 'docu_url', 'git_url', 'video_url']
    prepopulated_fields = {'project_slug': ('project_name',)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
