# Generated by Django 4.1.7 on 2023-03-12 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_hostuserprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HostUserProfile',
        ),
    ]