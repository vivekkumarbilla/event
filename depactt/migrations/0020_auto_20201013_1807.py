# Generated by Django 3.1 on 2020-10-13 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depactt', '0019_auto_20201013_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]
