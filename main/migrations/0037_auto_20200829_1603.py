# Generated by Django 3.0.8 on 2020-08-29 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20200828_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloud',
            name='used_percent',
            field=models.CharField(default=0, max_length=10, verbose_name='درصد استفاده شده'),
        ),
    ]
