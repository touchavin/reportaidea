from django.db import models
from django.utils.html import format_html
# Create your models here.


class User(models.Model):
    username=models.CharField(max_length=100, blank=True, null=True)
    email=models.EmailField(max_length=100, blank=True, null=True)
    first_name=models.CharField(max_length=100, blank=True, null=True)
    last_name=models.CharField(max_length=100, blank=True, null=True)
    password=models.CharField(max_length=50)
        
class Image(models.Model):
    
    Day = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    Office = models.CharField(max_length=100, blank=True, null=True)
    Circuit = models.CharField(max_length=100, blank=True, null=True)
    Accessory = models.CharField(max_length=100, blank=True, null=True)
    Case = models.CharField(max_length=100, blank=True, null=True)
    Customer_number = models.CharField(max_length=100, blank=True, null=True)
    pathimage = models.CharField(max_length=100, blank=True, null=True)  #เพิ่ม
    image = models.FileField(upload_to='media/', null=True, blank=True)
    

    def show_image(self): 
        if self.image:
            return format_html('<img src="%s" height="40px">' % self.image.url) 
        return ''
    show_image.allow_tags = True 
    show_image.short_description = 'Image'
