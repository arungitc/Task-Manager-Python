# Generated by Django 4.2 on 2024-10-10 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0006_remove_report_pdf_file_remove_report_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='subject',
            field=models.TextField(blank=True, max_length=240),
        ),
    ]
