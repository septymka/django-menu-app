from django.db import models

# Create your models here.
class Item(models.Model):
    """Food Item."""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.CharField(max_length=500, default="https://images.pexels.com/photos/940302/pexels-photo-940302.jpeg?auto=compress&cs=tinysrgb&w=300")

    def __str__(self):
        return self.name