from django.db import models

# Create your models here.

class Denomination(models.Model):
    code = models.CharField(max_length = 2, primary_key=True)
    name = models.CharField(max_length = 50)
    value = models.PositiveIntegerField()
    active = models.BooleanField()

    def __str__(self):
        return self.name
    
class Location(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length = 50)
    active = models.BooleanField()

    def __str__(self):
        return self.name

class SubLocation(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length = 50)
    active = models.BooleanField()
    def __str__(self):
        return self.name


class BoxType(models.Model):
    name = models.CharField(max_length = 50)
    number_of_bundles = models.SmallIntegerField()
    def __str__(self):
        return self.name


class Box(models.Model):
    box_number = models.CharField(max_length = 50)
    box_type = models.ForeignKey(BoxType, on_delete=models.CASCADE)
    denomination = models.ForeignKey(Denomination, on_delete=models.CASCADE)
    series_from = models.CharField(max_length = 3)
    serial_number_from = models.CharField(max_length = 7)
    series_to = models.CharField(max_length = 3)
    serial_number_to = models.CharField(max_length = 7)
    packing_date = models.DateField()
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        unique_together = [
            ['denomination', 'series_from', 'serial_number_from'],
            ['denomination', 'series_from', 'serial_number_to'],
            ['box_number', 'packing_date']
        ]

class Shipment(models.Model): 
    shipment_date = models.DateField()
    sent_from = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="shipments_sent")
    sent_to = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="shipments_received")
    boxes = models.ManyToManyField(Box, related_name = "shipments")
    is_delivered = models.BooleanField()

class Bundle(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name="bundles", null=True, blank=True)
    bundle_number_in_box = models.CharField(max_length = 2)
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE) 