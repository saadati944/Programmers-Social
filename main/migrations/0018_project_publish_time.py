# Generated by Django 3.0.8 on 2020-08-23 07:32

from django.db import migrations
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20200823_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='publish_time',
            field=django_jalali.db.models.jDateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار'),
        ),
    ]
