# Generated by Django 4.0.3 on 2022-03-11 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.FileField(default='download.jpg', upload_to='Profile'),
        ),
    ]