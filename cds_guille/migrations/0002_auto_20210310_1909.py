# Generated by Django 3.1.7 on 2021-03-10 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cds_guille', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='original',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]