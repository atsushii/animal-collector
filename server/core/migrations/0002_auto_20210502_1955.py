# Generated by Django 3.1.4 on 2021-05-02 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranimal',
            name='picture_url',
            field=models.FileField(upload_to=''),
        ),
    ]
