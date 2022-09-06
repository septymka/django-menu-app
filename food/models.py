from django.db import models

# Create your models here.
class Item(models.Model):
    """Food Item."""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name