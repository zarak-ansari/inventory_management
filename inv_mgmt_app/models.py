from django.db import models

# Create your models here.

class Denomination(models.Model):
    code = models.CharField(max_length = 3, primary_key=True)
    name = models.CharField(max_length = 50)
    value = models.PositiveIntegerField()
    active = models.BooleanField()

    def __str__(self):
        return self.name
    
class Location(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Box_Container(models.Model):
    shipment_date = models.DateField()
    sent_from = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="shipments_sent")
    sent_to = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="shipments_received")
    

class Box(models.Model):
    box_container = models.ForeignKey(Box_Container, on_delete=models.CASCADE, related_name="boxes")

class Bundle(models.Model):
    denomination = models.ForeignKey(Denomination, on_delete=models.CASCADE)
    series = models.CharField(max_length = 3)
    number = models.CharField(max_length = 4)
    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name="bundles")
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    barcode = models.ImageField()