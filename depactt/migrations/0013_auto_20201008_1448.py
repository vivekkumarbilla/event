# Generated by Django 3.1 on 2020-10-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depactt', '0012_auto_20201008_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pubdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
