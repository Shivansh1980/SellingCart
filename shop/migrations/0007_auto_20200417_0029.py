# Generated by Django 3.0.4 on 2020-04-17 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200417_0012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product',
            new_name='product_detail',
        ),
    ]