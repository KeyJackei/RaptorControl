# Generated by Django 5.1.1 on 2024-11-08 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RControl', '0011_remove_devicehost_uptime'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicehost',
            name='uptime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
