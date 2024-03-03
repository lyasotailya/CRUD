from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    measurements = models.ForeignKey(Measurement, on_delete=models.CASCADE, null=True)
