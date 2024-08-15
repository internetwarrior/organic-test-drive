from django.contrib import admin
from .models import Project, Tag

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('progress_bar', 'state', 'dao_project', 'xp', 'flag', 'kyc_verified')
    search_fields = ('state',)
    list_filter = ('state', 'dao_project', 'kyc_verified', 'flag')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created')
    search_fields = ('name',)