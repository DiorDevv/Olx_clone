# Generated by Django 5.1.6 on 2025-03-04 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0002_attributeoptions_alter_attribute_options_and_more'),
        ('olx_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='attributes',
            field=models.ManyToManyField(blank=True, to='attribute.attribute'),
        ),
        migrations.CreateModel(
            name='AdsAtribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(max_length=100)),
                ('ads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olx_app.ads')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.attribute')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdsAtributeOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olx_app.ads')),
                ('ads_atribute_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.attribute')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.attributeoptions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
