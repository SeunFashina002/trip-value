# Generated by Django 4.1.7 on 2023-03-02 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_alter_state_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='state',
            options={'ordering': ('state',)},
        ),
    ]
