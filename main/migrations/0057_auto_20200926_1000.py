# Generated by Django 3.0.8 on 2020-09-26 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0056_auto_20200926_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/', verbose_name='آواتار'),
        ),
    ]
