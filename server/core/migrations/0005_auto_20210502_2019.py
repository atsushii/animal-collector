# Generated by Django 3.1.4 on 2021-05-02 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210502_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranimal',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
