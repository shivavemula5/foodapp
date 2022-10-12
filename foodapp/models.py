from django.db import models

class Item(models.Model):
    def __str__(self):
        return self.item_name
    item_name = models.CharField(max_length = 200)
    item_desc = models.CharField(max_length = 200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length = 500 , default = "https://p.kindpng.com/picc/s/79-798754_hoteles-y-centros-vacacionales-dish-placeholder-hd-png.png")
