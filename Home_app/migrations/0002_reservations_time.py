# Generated by Django 4.1.4 on 2022-12-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='time',
            field=models.CharField(default=3, max_length=5),
            preserve_default=False,
        ),
    ]