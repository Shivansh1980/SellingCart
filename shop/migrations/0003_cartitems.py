# Generated by Django 3.0.4 on 2020-04-01 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200324_0142'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=20)),
                ('item_id', models.CharField(max_length=1000)),
                ('customer_name', models.CharField(max_length=40)),
            ],
        ),
    ]