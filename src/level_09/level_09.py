'''
Created on 2013-4-12

@author: nan
'''

from PIL import Image, ImageDraw

first = [int(i) for i in open("first.txt", "r").read().replace("\n", "").split(",")]
second = [int(i) for i in open("second.txt", "r").read().replace("\n", "").split(",")]

def run():
    draw()
    pass   

def draw():
    im = Image.open("good.jpg")
    
    draw = ImageDraw.Draw(im)
    
    draw.point(getCoordinates(first), fill=(255, 0, 0))
    draw.point(getCoordinates(second), fill=(255, 0, 0))
    del draw 
    
    im.save("good1.jpg", "JPEG")
    
def getCoordinates(context):
    coordinates = []
    yindex = 1;
    for xindex in range(context.__len__()):
        if xindex % 2 != 0:
            yindex += 2
            continue
        coordinates.append((context[xindex], context[yindex]))
    return coordinates

def better():
    img = Image.new('RGB', (640, 480))
    draw = ImageDraw.Draw(img)
    draw.line(first)
    draw.line(second)
    img.show()
