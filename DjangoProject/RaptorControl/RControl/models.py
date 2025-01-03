from django.db import models


class DeviceHost(models.Model):
    hostname = models.CharField(max_length=255)
    boot_time = models.DateTimeField()
    os = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    kernel_version = models.CharField(max_length=50)
    arch = models.CharField(max_length=50)
    uptime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.hostname

class DevicesClient(models.Model):
    client_id = models.CharField(max_length=128)
    hostname = models.CharField(max_length=255)
    os = models.CharField(max_length=50)
    release = models.CharField(max_length=50)
    last_ip = models.CharField(max_length=50)
    last_seen_at = models.DateTimeField()
    status = models.CharField(max_length=20, default='Inactive')

    def __str__(self):
        return self.hostname

