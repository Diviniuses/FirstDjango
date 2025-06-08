from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    description = models.TextField(default='')
    brand = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name
