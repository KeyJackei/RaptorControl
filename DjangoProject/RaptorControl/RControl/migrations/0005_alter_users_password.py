# Generated by Django 5.1.1 on 2024-10-14 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RControl', '0004_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
