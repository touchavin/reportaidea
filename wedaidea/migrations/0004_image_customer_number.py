# Generated by Django 3.2.4 on 2021-06-16 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedaidea', '0003_rename_patsimage_image_pathimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='Customer_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]