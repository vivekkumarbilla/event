# Generated by Django 3.1 on 2020-10-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depactt', '0009_auto_20201002_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='messagedate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='timee',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
