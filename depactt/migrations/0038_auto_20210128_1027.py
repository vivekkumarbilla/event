# Generated by Django 3.1 on 2021-01-28 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depactt', '0037_auto_20210106_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messaging',
            name='messageseen',
            field=models.BooleanField(default=False),
        ),
    ]
