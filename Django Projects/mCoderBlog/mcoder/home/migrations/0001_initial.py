# Generated by Django 3.0.4 on 2020-07-04 05:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=15)),
                ('email', models.CharField(default='', max_length=100)),
                ('content', models.TextField(default='')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
