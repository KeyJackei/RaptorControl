# Generated by Django 5.1.1 on 2025-02-03 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RControl', '0017_devicesclient_first_seen_at_devicesclient_fqdn_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicesclient',
            name='mac_addresses',
        ),
    ]
