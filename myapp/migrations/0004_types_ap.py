# Generated by Django 4.2 on 2023-05-22 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_apartmentdb_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Types_Ap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(blank=True, max_length=50, null=True)),
                ('Company_Name', models.CharField(blank=True, max_length=60, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Area', models.CharField(blank=True, max_length=100, null=True)),
                ('Type_Image', models.ImageField(blank=True, null=True, upload_to='Dp')),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]