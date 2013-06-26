'''
Created on 2013-4-15

@author: nan
'''

from PIL import Image



def run():
    img = Image.open("cave.jpg")
    hight, width = img.size
    for x in range(hight):
        for y in range(width):
            if x % 2 == 0 or y % 2 == 0:
                img.putpixel((x, y), (0, 0, 0))
    
    img.show()
    
def better1():
    import urllib
    from PIL import Image
    from cStringIO import StringIO
    def splitOE(source):
        results = []
        width, height = source.size
        results = [Image.new(source.mode, (width // 2, height // 2))
                   for dummy in range(4)]
        for x in range(width):
            for y in range(height):
                target = results[x % 2 + (y % 2 << 1)]
                target.putpixel((x // 2, y // 2), source.getpixel((x, y)))
        return results
    url = 'http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg'
    odd_even = splitOE(Image.open(StringIO(urllib.urlopen(url).read())))
    for result in odd_even:
        result.show()    

if __name__ == '__main__':
    run()
#    better1()
    print 'Done'
    pass
