# Generated by Django 3.0.4 on 2020-05-07 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20200507_0643'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderForm',
            new_name='OrderedProduct',
        ),
    ]