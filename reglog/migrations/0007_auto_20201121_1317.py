# Generated by Django 3.1 on 2020-11-21 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reglog', '0006_auto_20201121_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
