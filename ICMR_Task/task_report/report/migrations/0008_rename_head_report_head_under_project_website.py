# Generated by Django 4.2 on 2024-10-10 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0007_report_date_alter_report_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='head',
            new_name='head_under_project_website',
        ),
    ]
