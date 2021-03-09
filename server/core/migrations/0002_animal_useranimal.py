# Generated by Django 3.1.4 on 2021-03-09 01:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserAnimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_url', models.URLField()),
                ('x_coordinate', models.FloatField()),
                ('y_coordinate', models.FloatField()),
                ('animals', models.ManyToManyField(to='core.Animal')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
