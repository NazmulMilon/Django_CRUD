# Generated by Django 3.2.6 on 2021-08-22 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_contact_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='image',
        ),
    ]
