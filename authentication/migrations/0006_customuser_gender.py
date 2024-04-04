# Generated by Django 4.1.7 on 2024-03-13 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_hostuserprofile_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Non-Binary', 'non-binary')], default='female', max_length=20),
        ),
    ]