# Generated by Django 3.2 on 2021-04-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=900)),
                ('created_in', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='blog')),
            ],
        ),
    ]
