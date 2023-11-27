from django.db import models

class Grid(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Component(models.Model):
    name = models.CharField(max_length=200)
    component_type = models.CharField(max_length=100)
    value = models.FloatField()
    grid = models.ForeignKey(Grid, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
