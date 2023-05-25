import os
from PIL import Image

def crop_square(image):
    width, height = image.size
    
    if width > height:
        left = (width-height)/2
        top = 0
        right = width-(width-height)/2
        bottom = height
    else:
        left = 0
        top = (height-width)/2
        right = width
        bottom = height-(height-width)/2
    
    image = image.crop((left, top, right, bottom))
    return image


for main in os.listdir(r'dataset'):
    for image in os.listdir(r'dataset/{}'.format(main)):
        im = Image.open(r'dataset/{}/{}'.format(main, image)) 
        im = crop_square(im)
        im.save(r'dataset/{}/{}'.format(main, image))