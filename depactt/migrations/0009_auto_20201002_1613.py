# Generated by Django 3.1 on 2020-10-02 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depactt', '0008_auto_20201002_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='messagedate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='timee',
            field=models.TimeField(blank=True),
        ),
    ]
