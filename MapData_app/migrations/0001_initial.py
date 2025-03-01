# Generated by Django 4.2.2 on 2025-02-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=260)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
