from django.contrib import admin
from.models import  Image
from.models import  Report


class ImageAdmin(admin.ModelAdmin):
    list_display = ['Day', 'Time', 'Customer_number', 'Accessory', 'Case', 'Circuit', 'pathimage', 'pathoraclecloud', 'show_image']
    list_filter = ['Case']
    search_fields = ['Accessory', 'Case', 'Circuit']


class ReportAdmin(admin.ModelAdmin):
    list_display = ['Day', 'Time', 'Partner', 'Zpm4', 'Powerstation', 'Branch', 'Power', 'Circuit', 'Distance', 'GPS', 'pathoraclecloud', 'show_image']
    list_filter = ['Zpm4']
    search_fields = ['Zpm4', 'Power', 'Circuit']




admin.site.register(Image, ImageAdmin)
admin.site.register(Report, ReportAdmin)
