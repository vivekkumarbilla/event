# Generated by Django 3.1 on 2020-11-04 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('depactt', '0028_groupmembers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmessages',
            name='groupref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='depactt.groupmembers'),
        ),
        migrations.DeleteModel(
            name='Grouping',
        ),
    ]
