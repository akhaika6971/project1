# Generated by Django 4.1.7 on 2023-10-20 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_hostuserprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostuserprofile',
            name='company_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
