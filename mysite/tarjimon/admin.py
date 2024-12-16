from django.contrib import admin
from . import models


class LugatAdmin(admin.ModelAdmin):
    list_display = ['ing', 'uzb']

admin.site.register(models.Lugat, LugatAdmin)
