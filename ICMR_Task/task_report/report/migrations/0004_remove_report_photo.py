# Generated by Django 4.2 on 2024-10-10 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_alter_report_subject_alter_report_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='photo',
        ),
    ]
