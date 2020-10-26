from django.db import models
from django.contrib.postgres.fields import JSONField
import random
import string

def list_check_types():
    check_types_list=[(u'kitchen',u'kitchen'),
                        (u'client',u'client') ]
    return check_types_list

API_LEN = 40

def base_str():
    return (string.ascii_letters+string.digits)   
def api_key():
    keylist = [random.choice(base_str()) for i in range(API_LEN)]
    return ("".join(keylist))

def list_status_types():
    status_types_list=[(u'new',u'new'),
                        (u'rendered',u'rendered'),
                        (u'printed',u'printed') ]
    return status_types_list

class Printer(models.Model):
    name = models.CharField(max_length=120)
    api_key = models.CharField(max_length=120, default=api_key)
    check_type = models.CharField(max_length=120, choices=list_check_types(), blank=False, null=False)
    point_id = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + self.check_type

class Check(models.Model):
    printer_id = models.ForeignKey('Printer', on_delete=models.CASCADE, blank=False, null=False)
    type = models.CharField(max_length=120, choices=list_check_types(), blank=False, null=False)
    order = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=120, choices=list_status_types(), blank=False, null=False)
    pdf_file = models.FileField

    def __str__(self):
        return self.type + ' ' + self.status