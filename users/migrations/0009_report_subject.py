# Generated by Django 5.0.2 on 2024-04-21 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_description_report_reportdescription_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='subject',
            field=models.CharField(default='No Subject', max_length=255),
        ),
    ]