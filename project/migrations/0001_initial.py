# Generated by Django 5.0.1 on 2024-01-13 12:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_identifier', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=50)),
                ('college', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('level', models.IntegerField()),
                ('contact_info', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=50)),
                ('matric_number', models.CharField(max_length=10, unique=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('cgpa', models.FloatField()),
                ('admission_type', models.CharField(max_length=20)),
                ('scholarship_info', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('passport_photograph', models.ImageField(blank=True, null=True, upload_to='passport_photos/')),
            ],
        ),
    ]
