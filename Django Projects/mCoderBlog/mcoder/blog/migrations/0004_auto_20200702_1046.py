# Generated by Django 3.0.4 on 2020-07-02 05:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200702_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 5, 16, 42, 249699, tzinfo=utc)),
        ),
    ]
