from django.db import models
from django.contrib.postgres.fields import JSONField

class Printer(models.Model):
    name = models.CharField(max_length=120)
    api_key = models.CharField(max_length=120)
    check_type = models.CharField(max_length=120)
    point_id = models.IntegerField()

    def __str__(self):
        return self.name

class Check(models.Model):
    printer_id = models.ForeignKey('Printer', on_delete=models.CASCADE, blank=False, null=False)
    type = models.CharField(max_length=120)
    order = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=120)
    pdf_file = models.FileField