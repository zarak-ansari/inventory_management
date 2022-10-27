import os

from django.shortcuts import render
from django.conf import settings
from django.http import FileResponse

from .forms import BundleGenerationForm
from .models import Bundle
from . import barcode_helpers

MEDIA_DIR = settings.MEDIA_DIR

# Create your views here.
def index(request):
    return render(request, "index.html")

def generate_bundles(request):
    context = {}

    if request.method == 'POST':
        form = BundleGenerationForm(request.POST)

        if form.is_valid():
            serial_from = form.cleaned_data.get("starting_serial")
            number_of_bundles = form.cleaned_data.get("number_of_bundles")
            barcodes_list = []
            for i in range(number_of_bundles):
                bundle_obj = Bundle()
                bundle_obj.denomination = form.cleaned_data.get("denomination")
                bundle_obj.series = form.cleaned_data.get("series")
                bundle_obj.serial_number = str(int(serial_from) + i).rjust(4,"0") 
                bundle_obj.current_location = form.cleaned_data.get("location")
                bundle_obj.packing_date = form.cleaned_data.get("packing_date")
                bundle_obj.save()
                barcode_string = barcode_helpers.generate_barcode_for_bundle(bundle_obj, MEDIA_DIR)
                barcodes_list.append(barcode_string)
            barcode_helpers.image_list_to_pdf(barcodes_list, MEDIA_DIR)
            
            return FileResponse(open(os.path.join(MEDIA_DIR, barcodes_list[0] + ".pdf"), "rb"), as_attachment=True, content_type="application/pdf")
    else:
        form = BundleGenerationForm()
    
    context['form'] = form

    return render(request, "generate_bundles.html", context=context)

def create_box(request):
    pass