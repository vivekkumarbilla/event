# Generated by Django 3.1 on 2021-01-06 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depactt', '0035_auto_20210105_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messaging',
            name='messageseen',
            field=models.CharField(default='first', max_length=200),
        ),
    ]