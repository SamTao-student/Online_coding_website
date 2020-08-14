# Generated by Django 3.1 on 2020-08-14 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('内容', models.TextField()),
                ('author', models.CharField(max_length=10)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('点赞数', models.IntegerField()),
                ('class_choice', models.CharField(choices=[('yes', '是'), ('no', '否')], max_length=10)),
            ],
        ),
    ]