# Generated by Django 3.2.4 on 2021-07-01 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedaidea', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.DateField(auto_now_add=True)),
                ('Time', models.TimeField(auto_now_add=True)),
                ('Partner', models.CharField(blank=True, max_length=100, null=True)),
                ('Zpm4', models.CharField(blank=True, max_length=100, null=True)),
                ('Powerstation', models.CharField(blank=True, max_length=100, null=True)),
                ('Branch', models.CharField(blank=True, max_length=100, null=True)),
                ('Power', models.CharField(blank=True, max_length=100, null=True)),
                ('Circuit', models.CharField(blank=True, max_length=100, null=True)),
                ('Distance', models.FloatField(blank=True, default=0.0, null=True)),
                ('GPS', models.FloatField(blank=True, default=0.0, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
