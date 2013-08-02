'''
Created on 2013-7-29

@author: nan
'''
# http://www.pythonchallenge.com/pc/return/mozart.html

from PIL import Image

def straighten(line):  # five equal consecutive pink pixels are the clue
    idx = 0
    while line[idx] != 195:
        idx += 1
    return line[idx:] + line[:idx]

# url = 'http://huge:file@www.pythonchallenge.com/pc/return/mozart.gif'
# im = Image.open(cStringIO.StringIO(urllib.urlopen(url).read()))
im = Image.open("mozart.gif");
for y in range(im.size[1]):
    line = [im.getpixel((x, y)) for x in range(im.size[0])]
    line = straighten(line)
    [im.putpixel((x, y), line[x]) for x in range(len(line))]
im.show()

# romance
