# Generated by Django 2.2.1 on 2020-10-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200917_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Bio',
            field=models.TextField(blank=True, help_text="Ex: Etudiant (Ingenieur Informatique...) en master de science politique à l'université Felix Houphouet Boigny", max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='Ecole',
            field=models.CharField(blank=True, help_text='Ex: Université Nangui Abrogoua', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name="niveau d'etude",
            field=models.CharField(blank=True, choices=[('L1', 'Licence 1'), ('1ere annee', '1ère année'), ('L2', 'Licence 2'), ('2ere annee', '2ième année'), ('AS', 'AS'), ('ITS', 'ITS'), ('ISE', 'ISE'), ('L3', 'Licence 3'), ('3ere annee', '3ième année'), ('M1', 'Master 1'), ('4ere annee', '4ième année'), ('M2', 'Master 2'), ('5ere annee', '5ième année'), ('DOCTORANT', 'Doctorant')], max_length=30),
        ),
    ]
