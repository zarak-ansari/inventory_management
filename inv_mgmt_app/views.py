import os

from django.shortcuts import render
from django.conf import settings
from django.http import FileResponse

from .forms import BoxForm, BundleGenerationForm
from .models import Bundle
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