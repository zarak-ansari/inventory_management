from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image
import os
from django.conf import settings

from .models import Box, Bundle

def generate_and_save_barcode(input_string: str, path):
    options = {
        "quiet_zone":12,
        "font_size":11
    }
    location = os.path.join(path, input_string)
    Code128(input_string, writer=ImageWriter()).save(location, options=options)

def image_list_to_pdf(img_filename_list, path):
    
    image_1 = Image.open(os.path.join(path, img_filename_list[0] + ".png")).convert("RGB")

    image_2_onwards = []
    for image in img_filename_list[1:]:
        image = Image.open(os.path.join(path, image + ".png")).convert("RGB")
        image_2_onwards.append(image)
    path_to_pdf = os.path.join(path, img_filename_list[0]+".pdf")
    image_1.save(path_to_pdf, save_all=True, append_images = image_2_onwards)
    return path_to_pdf

def generate_barcode_for_bundle(bundle: Bundle, path):
    date_string = bundle.box.packing_date.strftime("%Y%m%d")
    box_number = bundle.box.box_number
    bundle_number = bundle.bundle_number_in_box
    barcode_string = date_string + box_number + bundle_number
    generate_and_save_barcode(barcode_string, path)
    return barcode_string

def generate_barcode_for_box(box: Box, path):
    date_string = box.packing_date.strftime("%Y%m%d")
    denomination = box.denomination.code
    box_number = box.box_number
    box_barcode_string = date_string + denomination + box_number
    generate_and_save_barcode(box_barcode_string, path)

    barcode_list = []
    barcode_list.append(box_barcode_string)
    barcode_list.append(box_barcode_string)
    
    for bundle in box.bundles.all():
        bundle_barcode_string = generate_barcode_for_bundle(bundle, path)
        barcode_list.append(bundle_barcode_string)
    file_location = image_list_to_pdf(barcode_list, path)
    return file_location