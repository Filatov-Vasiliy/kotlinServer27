# Generated by Django 4.2.8 on 2023-12-20 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_newsheaders_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsheaders',
            name='newsSection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='headers', to='api.newssection'),
        ),
        migrations.AlterField(
            model_name='newssection',
            name='newsChannel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='api.newschannels'),
        ),
    ]
