# Generated by Django 2.1.1 on 2021-02-01 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0009_auto_20210112_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='image',
            field=models.ImageField(default=None, upload_to='crud_curso/images/'),
        ),
    ]
