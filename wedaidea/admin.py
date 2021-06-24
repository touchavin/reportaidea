from django.contrib import admin
from.models import  Image



class ImageAdmin(admin.ModelAdmin):
    list_display = ['Day', 'Time', 'Customer_number', 'Accessory', 'Case', 'Circuit', 'pathimage', 'show_image']
    list_filter = ['Case']
    search_fields = ['Accessory', 'Case', 'Circuit']






admin.site.register(Image, ImageAdmin)