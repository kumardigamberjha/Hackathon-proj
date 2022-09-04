from django.contrib import admin
from website.resource import SalaryResources
from website.models import DBModel
from import_export.admin import ImportExportModelAdmin

@admin.register(DBModel)
class DBModelAdmin(ImportExportModelAdmin):
    pass