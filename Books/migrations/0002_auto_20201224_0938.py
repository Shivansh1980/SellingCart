# Generated by Django 3.0.4 on 2020-12-24 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(upload_to='books/images'),
        ),
    ]
