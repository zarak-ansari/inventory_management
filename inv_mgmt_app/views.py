import os

from django.shortcuts import render
from django.conf import settings
from django.http import FileResponse, HttpResponse
from django.db.models import Count

from .forms import GetBoxesForm, BoxForm, ShipmentForm
from .models import Box, Bundle, Denomination, Shipment
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
        boxes_form = GetBoxesForm(request.POST)
        if form.is_valid() and boxes_form.is_valid():
            shipment = form.save()
            box_codes = boxes_form.cleaned_data['boxes'].split()
            for box_code in box_codes:
                b = barcode_helpers.get_box_from_barcode_string(box_code)
                shipment.boxes.add(b)
    else:
        form = ShipmentForm()
        boxes_form = GetBoxesForm()

    context['form'] = form
    context['boxes_form'] = boxes_form

    return render(request, "create_shipment.html", context=context)

def show_shipment_detail(request, shipment_id):
    
    try:
        shipment = Shipment.objects.get(id=shipment_id)
    except:
        return HttpResponse("Invalid Shipment ID in URL")

    boxes = shipment.boxes.all()
    context = {
        'shipment' : shipment,
        'boxes' : boxes
    }
    denom_wise_count = boxes.values('denomination').annotate(dcount=Count('denomination')).order_by()
    for record in denom_wise_count:
        record['denomination_name'] = Denomination.objects.get(code=record['denomination']).name
    # print(denom_wise_count)
    context['denom_wise_count'] = denom_wise_count
    return render(request, "show_shipment_detail.html", context=context)

def receive_shipment(request, shipment_id):
    return HttpResponse("Under Construction")