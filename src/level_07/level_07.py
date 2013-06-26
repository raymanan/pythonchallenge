'''
Created on 2013-4-12

@author: nan
'''
from PIL import Image
import urllib, StringIO

def run():
    level7_2()
    
def level7():
    img = Image.open('oxygen.png')
#    output = StringIO.StringIO()
#    img.save(output, format="PNG")
#    imgContext = output.getvalue()
#    output.close()
    
#    f = open("oxygen.txt", 'w')
#    f.write(img.tostring())
# #    p=re.compile(r'[a-z]{2}[?]')
    imgContext = img.tostring()
    
    result = ""
#    print imgContext
    for index in range(0, len(imgContext) - 2):
        if (imgContext[index] == imgContext[index + 1] == imgContext[index + 2]):
            result = result + imgContext[index]
            index = index + 2
#            print imgContext[index] + imgContext[index + 1] + imgContext[index + 2]
    print "result= " + result
#    print re.findall(p,img.tostring())
        
    nextlevel = (105, 110, 116, 101, 103, 114, 105, 116, 121)
    print "".join(chr(i) for i in nextlevel);
#    for i in nextlevel[:]:
#        print chr(i)
#    print (chr(i) for i in nextlevel)
    
def level7_1():
    print Image.open('oxygen.png').tostring()[108188:110620:28]
    
def level7_2():
    img = urllib.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()
    i = Image.open(StringIO.StringIO(img))  # Image.open requires a file-like object
    i.size
    [i.getpixel((x, 45)) for x in range(629)]
    row = [i.getpixel((x, 45)) for x in range(0, i.size[0], 7)]
    ords = [r for r, g, b, a in row if r == g == b]
    print "".join(map(chr, ords))
