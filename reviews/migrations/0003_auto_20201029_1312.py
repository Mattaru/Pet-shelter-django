# Generated by Django 3.1.2 on 2020-10-29 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20201029_1310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='my_id',
            new_name='id',
        ),
    ]
