# Generated by Django 3.1 on 2021-01-05 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depactt', '0033_auto_20210105_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messaging',
            name='poster',
            field=models.ImageField(blank=True, upload_to='sharing'),
        ),
    ]
