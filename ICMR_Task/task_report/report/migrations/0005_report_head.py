# Generated by Django 4.2 on 2024-10-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_remove_report_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='head',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
