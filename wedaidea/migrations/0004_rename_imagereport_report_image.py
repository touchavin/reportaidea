# Generated by Django 3.2.4 on 2021-07-01 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedaidea', '0003_auto_20210701_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='imageReport',
            new_name='image',
        ),
    ]