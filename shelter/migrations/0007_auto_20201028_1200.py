# Generated by Django 3.1.2 on 2020-10-28 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0006_auto_20201024_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(default='unknown.png', upload_to='employees_photo/', verbose_name='Photo'),
        ),
    ]