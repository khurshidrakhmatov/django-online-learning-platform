# Generated by Django 3.2 on 2021-04-18 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_homework_homework_instruction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeworksubmission',
            name='submission_file_upload',
            field=models.FileField(upload_to='homework/'),
        ),
    ]