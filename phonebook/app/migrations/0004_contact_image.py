# Generated by Django 3.2.6 on 2021-08-23 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_contact_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]
