# Generated by Django 3.0.2 on 2020-08-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reglog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('pin', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='profilephoto')),
            ],
            options={
                'db_table': 'userdetails',
            },
        ),
    ]
