# Generated by Django 3.0.4 on 2020-05-06 10:20

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_orderform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderform',
            name='mobile_no',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
