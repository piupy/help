# Generated by Django 3.0.4 on 2020-06-21 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_category2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category2',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
