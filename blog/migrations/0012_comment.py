# Generated by Django 3.1 on 2020-08-23 16:10

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200823_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', mdeditor.fields.MDTextField()),
                ('author', models.CharField(max_length=100)),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
