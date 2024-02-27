# Generated by Django 5.0.2 on 2024-02-27 00:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
            ],
        ),
    ]
