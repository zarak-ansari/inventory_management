from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image
import os
from django.conf import settings


# Write to a file-like object:

def generate_and_save_barcode(input_string, path):
    options = {
        "quiet_zone":15,
        "font_size":11
    }
    location = os.path.join(path, input_string)
    Code128(input_string, writer=ImageWriter()).save(location, options=options)

def generate_barcode_for_bundle(bundle, path):
    date_string = "20221024"
    barcode_string = bundle.denomination_id + "-" + bundle.current_location_id + "-" + date_string + "-" + bundle.series + bundle.serial_number
    generate_and_save_barcode(barcode_string, path)
    return barcode_string

def image_list_to_pdf(img_filename_list, path):
    
    im_1 = Image.open(os.path.join(path, img_filename_list[0] + ".png")).convert("RGB")

    im_2_onwards = []
    for im in img_filename_list[1:]:
        image = Image.open(os.path.join(path, im + ".png")).convert("RGB")
        im_2_onwards.append(image)
    
    im_1.save(os.path.join(path, img_filename_list[0]+".pdf"), save_all=True, append_images = im_2_onwards)

# image_list_to_pdf(["12345678.png", "1234567890.png", "another_file.png", "somefile.png"])