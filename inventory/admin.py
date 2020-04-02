from django.contrib import admin
from . import models

@admin.register(models.Employees)
class BEmployeesAdmin(admin.ModelAdmin):
    pass