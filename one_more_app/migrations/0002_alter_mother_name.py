# Generated by Django 3.2.5 on 2022-10-08 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one_more_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mother',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
