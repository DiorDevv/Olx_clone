# Generated by Django 5.1.6 on 2025-03-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx_app', '0002_subcategory_attributes_adsatribute_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsatribute',
            name='value',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
