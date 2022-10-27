from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Box, Denomination, Location

class BundleGenerationForm(forms.Form):
    denomination = forms.ModelChoiceField(queryset=Denomination.objects.filter(active=True)) 
    location = forms.ModelChoiceField(queryset=Location.objects.all())
    series = forms.CharField(max_length=3)
    starting_serial = forms.CharField(min_length=4, max_length=4)
    number_of_bundles = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(50000)])
    packing_date = forms.DateField(widget=forms.SelectDateWidget())

# class BoxForm(forms.ModelForm):
#     class Meta:
#         model= Box
#         fields = ()