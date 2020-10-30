# Generated by Django 3.1.2 on 2020-10-30 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='Author name')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('message_data', models.TextField(verbose_name='Message')),
            ],
        ),
    ]
