import os

from django.shortcuts import render
from django.conf import settings
from django.http import FileResponse

from .forms import AddBoxesInShipmentForm, BoxForm, ShipmentForm
from .models import Box, Bundle
from . import barcode_helpers

MEDIA_DIR = settings.MEDIA_DIR

def index(request):
    return render(request, "index.html")

def generate_box(request):
    context = {}
    if request.method == 'POST':
        form = BoxForm(request.POST)
        if form.is_valid():
            box = form.save()
            number_of_bundles = box.box_type.number_of_bundles
            for i in range(number_of_bundles):
                bundle = Bundle(box = box, bundle_number_in_box = str(i).rjust(2,'0'), current_location = box.current_location)
                bundle.save()
            barcode_file_path = barcode_helpers.generate_barcode_for_box(box, MEDIA_DIR)
            return FileResponse(open(barcode_file_path, "rb"), as_attachment=True, content_type="application/pdf")
    else:
        form = BoxForm()
    
    context['form'] = form

    return render(request, "generate_box.html", context=context)

def create_shipment(request):
    context = {}
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        boxes_form = AddBoxesInShipmentForm(request.POST)
        if form.is_valid() and boxes_form.is_valid():
            shipment = form.save()
            box_codes = boxes_form.cleaned_data["boxes"].split() #boxes.split()
            for box_code in box_codes:
                b = barcode_helpers.get_box_from_barcode_string(box_code)
                shipment.boxes.add(b)
    else:
        form = ShipmentForm()
        boxes_form = AddBoxesInShipmentForm()

    context['form'] = form
    context['boxes_form'] = boxes_form

    return render(request, "create_shipment.html", context=context)