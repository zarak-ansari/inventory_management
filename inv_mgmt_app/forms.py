from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Box, Shipment

class BoxForm(forms.ModelForm):
    class Meta:
        model = Box
        exclude = ()
        widgets = {
            "packing_date": forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'})
        }


class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        exclude = ('boxes',)
        widgets = {
            "shipment_date": forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'})
        }
        

class AddBoxesInShipmentForm(forms.Form):
    boxes = forms.CharField(widget=forms.Textarea)
    
