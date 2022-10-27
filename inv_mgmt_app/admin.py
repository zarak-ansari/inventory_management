from django.contrib import admin
from .models import Box_Type, Bundle, Denomination, Location

# Register your models here.

admin.site.register(Denomination)
admin.site.register(Location)
admin.site.register(Bundle)
admin.site.register(Box_Type)
