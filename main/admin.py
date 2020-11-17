from django.contrib import admin
from main.models import *
from django.utils.html import format_html
import urllib
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User, Group
from import_export.admin import ExportActionModelAdmin
from .resources import *
from import_export.admin import ImportExportModelAdmin


models = [Arc]

#@admin.site.unregister(Transcript)

@admin.register(Transcript)
class TranscriptAdmin(ImportExportModelAdmin):
	search_fields = ['bitsID','refNo']
	resource_class = TranscriptResource

@admin.register(Gradesheet)
class GradesheetAdmin(ImportExportModelAdmin):
    search_fields = ['bitsID','refNo']
    resource_class = GradesheetResource

# @admin.register(Project)
# class ProjectAdmin(ExportActionModelAdmin,admin.ModelAdmin):
#     search_fields = ['faculty__name','department']
#     resource_class = ProjectResource

admin.site.register(models)
admin.site.unregister(Group)
