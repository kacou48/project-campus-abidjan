# Generated by Django 2.2.1 on 2020-10-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201007_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='forum',
            field=models.CharField(blank=True, choices=[('INFO', 'Info-Publique'), ('MI', 'Math-Info'), ('HIST', 'Histoire'), ('Geo', 'Geographie'), ('MED', 'Medecine'), ('PC', 'Physique-Chimie'), ('STRM', 'Strm-Cbg'), ('S-ECO', 'Science-Eco'), ('ANG', 'Anglais'), ('DROIT', 'Droit'), ('All', 'Allemand'), ('ESPA', 'Espagnole'), ('PHILO', 'Philosophie')], max_length=3),
        ),
    ]