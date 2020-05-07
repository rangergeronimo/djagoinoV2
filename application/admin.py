from django.contrib import admin

from .models import Sensor


class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind')
    ordering = ['name']
    list_filter = ['name', 'kind', 'id']


admin.site.register(Sensor, SensorAdmin)
