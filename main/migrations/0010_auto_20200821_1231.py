# Generated by Django 3.0.8 on 2020-08-21 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200821_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notif_type',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
