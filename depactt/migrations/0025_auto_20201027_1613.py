# Generated by Django 3.1 on 2020-10-27 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('depactt', '0024_remove_preevent_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouping',
            name='member1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_member_first', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='member10',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_member_tenth', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='member11',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_member_eleventh', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='member2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_member_second', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='member3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_member_third', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='member4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_member_fourth', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='member5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_member_fifth', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='member6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_member_sixth', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='member7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_member_seventh', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='member8',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_member_eighth', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='member9',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_member_ninth', to=settings.AUTH_USER_MODEL),
        ),
    ]