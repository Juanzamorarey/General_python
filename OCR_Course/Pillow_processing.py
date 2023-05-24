import cv2 #import openCV
from PIL import Image#import pillow
import pytesseract


im_file = "imagen_ejemplo.png"

im = Image.open(im_file)

#See data of the object that contains the image
# print(im)
# <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=2592x1458 at 0x1698E6CD0>


#See the actual image
# im.show()

#With this we can manage our image. FOr example rotate it.
# im.rotate(90).show()


#Once you've processed the image you might want to save it. It's done like this
im.save("temp/spacy_cheatsheet.png")