# Generated by Django 5.1.1 on 2024-10-03 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=255)),
                ('uptime', models.IntegerField()),
                ('boot_time', models.DateTimeField()),
                ('procs', models.IntegerField()),
                ('os', models.CharField(max_length=50)),
                ('platform', models.CharField(max_length=50)),
                ('kernel_version', models.CharField(max_length=50)),
                ('arch', models.CharField(max_length=50)),
            ],
        ),
    ]
