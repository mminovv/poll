# Generated by Django 3.2.7 on 2022-01-14 22:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_statistic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 14, 22, 31, 7, 635261, tzinfo=utc), editable=False),
        ),
    ]
