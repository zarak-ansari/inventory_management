from django import forms

from .models import Denomination, Location

class BundleGenerationForm(forms.Form):
    denom = forms.ModelChoiceField(queryset=Denomination.objects.all()) 
    location = forms.ModelChoiceField(queryset=Location.objects.all())
    series = forms.CharField(max_length=3)
    date_of_packing = forms.DateField(widget=forms.SelectDateWidget())

