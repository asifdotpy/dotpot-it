# Generated by Django 4.1.6 on 2023-02-19 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('cover_letter', models.TextField(verbose_name='Cover Letter')),
                ('resume', models.FileField(upload_to='resumes/', verbose_name='Resume')),
                ('job_title', models.CharField(max_length=255, verbose_name='Job Title')),
                ('activation_key', models.CharField(max_length=32, unique=True, verbose_name='Activation Key')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Job Application',
                'verbose_name_plural': 'Job Applications',
            },
        ),
    ]
