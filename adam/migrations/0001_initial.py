# Generated by Django 2.0 on 2017-12-12 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_published', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('author_user', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]