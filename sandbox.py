# from barcode import Code128
# from barcode.writer import ImageWriter

# # Write to a file-like object:
# num = "A12345678901234567890123A" #01234567890"

# options = {
#     "quiet_zone":15,
#     "font_size":12
# }

# Code128(num, writer=ImageWriter()).save("another_file", options)

from PIL import Image

im1 = Image.open("another_file.png")
im2 = Image.open("somefile.jpeg")
im3 = Image.open("another_file.png")


im_list = [im2, im3]

im1.convert("RGB")
im2.convert("RGB")
im3.convert("RGB")

im1.save("somefile.pdf", save_all=True, append_images = im_list)

