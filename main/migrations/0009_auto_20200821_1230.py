# Generated by Django 3.0.8 on 2020-08-21 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_notification_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='type',
            new_name='notif_type',
        ),
    ]
