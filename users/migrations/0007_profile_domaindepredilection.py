# Generated by Django 2.2.1 on 2020-11-05 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_profession'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='DomainDePredilection',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
