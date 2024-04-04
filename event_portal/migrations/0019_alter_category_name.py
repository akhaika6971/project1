# Generated by Django 4.1.7 on 2023-03-06 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_portal', '0018_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Conferences', 'Conferences'), ('Trade Shows', 'Trade Shows'), ('Networking', 'Networking'), ('WorkShops', 'WorkShops'), ('Product Launch', 'Product Launch'), ('Charity', 'Charity'), ('Music', 'Music'), ('Concert', 'Concert'), ('Performing & Visual Arts', 'Performing & Visual Arts'), ('Food & Drink', 'Food & Drink'), ('Party', 'Party'), ('Sports & Fitness', 'Sports & Fitness'), ('Technology', 'Technology'), ('Digital', 'Digital')], max_length=40, unique=True),
        ),
    ]
