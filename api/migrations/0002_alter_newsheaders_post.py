# Generated by Django 4.2.8 on 2023-12-20 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsheaders',
            name='post',
            field=models.CharField(max_length=500),
        ),
    ]
