from django.db import models
from django.urls import reverse

# Create your models here.

class Chart(models.Model):
    FORMS = [
    ('S', 'Шестигранник'),
    ('R', 'Круг'),
    ]
    form = models.CharField(max_length=1, choices=FORMS,default='R',)
    diameter = models.CharField(max_length=255)
    # value = models.FloatField(blank=True, null=True)
    value1 = models.FloatField(blank=True, null=True)
    value2 = models.FloatField(blank=True, null=True)
    value3 = models.FloatField(blank=True, null=True)
    time_measure = models.DateField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    kd = models.ForeignKey('Kind', on_delete=models.PROTECT, null=True)
    con = models.ForeignKey('Consumer', on_delete=models.PROTECT, null=True)
    gr = models.ForeignKey('Grade', on_delete=models.PROTECT, null=True, verbose_name="Марка стали")

    def __str__(self):
        return str(self.id)


class Kind(models.Model):
    # objects = None
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

class Consumer(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

class Grade(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name