from django.contrib import admin
from .models import Box, BoxType, Bundle, Denomination, Location, Shipment

# Register your models here.

admin.site.register(Denomination)
admin.site.register(Location)
admin.site.register(Bundle)
admin.site.register(BoxType)
admin.site.register(Box)
admin.site.register(Shipment)
