# Generated by Django 3.1 on 2020-08-13 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0005_auto_20200813_1941'),
        ('login', '0007_auto_20200813_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='own_class',
            field=models.ManyToManyField(to='backstage.Class'),
        ),
    ]
