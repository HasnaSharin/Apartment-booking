# Generated by Django 4.2 on 2023-05-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_apartmentdb_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartmentdb',
            name='Category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
