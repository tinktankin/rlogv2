# Generated by Django 3.1 on 2020-08-26 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0012_remove_pipeline_class_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipeline_class',
            name='Current_status_no',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]
