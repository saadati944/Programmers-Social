# Generated by Django 3.0.8 on 2020-08-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200819_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ads',
            field=models.BooleanField(default=False),
        ),
    ]
