# Generated by Django 4.1.4 on 2023-01-23 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_userprofile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='users/cover_photos'),
        ),
    ]
