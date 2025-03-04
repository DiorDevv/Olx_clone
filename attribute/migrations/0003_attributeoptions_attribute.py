# Generated by Django 5.1.6 on 2025-03-04 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0002_attributeoptions_alter_attribute_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributeoptions',
            name='attribute',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='attribute.attribute'),
            preserve_default=False,
        ),
    ]
