# Generated by Django 4.0.5 on 2023-03-01 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='locations',
            options={'ordering': ('state',)},
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.state')),
            ],
        ),
    ]
