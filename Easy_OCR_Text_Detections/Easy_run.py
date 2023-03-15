import os
import easyocr
reader  = easyocr.Reader(['en'])

import PIL
from PIL import ImageDraw

image = os.getcwd() + "/Easy_OCR_Text_Detections/Images/image_1.jpg"
img = PIL.Image.open(image)

bound = reader.readtext(image)
print(bound)