from django.db import models
from django.utils import timezone
from uuidfield import UUIDField

class raspi(models.Model):
    pos_x = models.FloatField(default = 0.0)
    pos_y = models.FloatField(default = 0.0)
    raspi_ID = models.IntegerField(default = 0, unique = True)

class device(models.Model):
    mac_ID = models.CharField(default = "", max_length = 100, unique = True)
    pos_x = models.FloatField(default = 0.0)
    pos_y = models.FloatField(default = 0.0)
    # updated = models.BooleanField(default = False)

class frame(models.Model):
    dev = models.ForeignKey(device)
    raspi = models.ForeignKey(raspi)
    signal = models.FloatField(default = 0.0)


# Create your models here.
