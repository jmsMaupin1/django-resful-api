from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=150)
    website = models.URLField(max_length=200)


class ShoeType(models.Model):
    style = models.CharField(max_length=50)

class ShoeColor(models.Model):
    RED = 'RED'
    ORANGE = 'ORANGE'
    YELLOW = 'YELLOW'
    GREEN = 'GREEN'
    BLUE = 'BLUE'
    INDIGO = 'INDIGO'
    VIOLET = 'VIOLET'
    WHITE = 'WHITE'
    BLACK = 'BLACK'

    COLOR_CHOICES = [
        (RED, 'Red'),
        (ORANGE, 'Orange'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (INDIGO, 'Indigo'),
        (VIOLET, 'Violet'),
        (WHITE, 'White'),
        (BLACK, 'Black'),
    ]

    color = models.CharField(
        max_length=50,
        choices=COLOR_CHOICES,
        default=RED
    )

class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    fasten_type = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE
    )
    color = models.ForeignKey(
        ShoeColor, on_delete=models.CASCADE
    )
    shoe_type = models.ForeignKey(
        ShoeType, on_delete=models.CASCADE
    )
