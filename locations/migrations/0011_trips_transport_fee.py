# Generated by Django 4.0.5 on 2023-03-02 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0010_remove_trips_date_of_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='trips',
            name='transport_fee',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
