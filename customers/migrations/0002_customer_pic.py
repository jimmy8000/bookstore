# Generated by Django 5.0.6 on 2024-05-15 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='pic',
            field=models.ImageField(default='no_picture.jpg', upload_to='customers'),
        ),
    ]