# Generated by Django 2.2.1 on 2020-09-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(default=2, upload_to='images_p'),
            preserve_default=False,
        ),
    ]
