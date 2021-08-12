from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=60, unique=True)
    description = models.TextField(max_length=200, default="Descripcion")
    image_url = models.CharField(max_length=200, default="https://images.freeimages.com/images/large-previews/5fb/wool-1-1530392.jpg")
    price = models.IntegerField(default=1000)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return self.name
