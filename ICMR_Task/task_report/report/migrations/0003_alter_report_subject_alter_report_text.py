# Generated by Django 4.2 on 2024-10-10 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_remove_report_status_report_name_of_institutes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='subject',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='report',
            name='text',
            field=models.TextField(max_length=100),
        ),
    ]
