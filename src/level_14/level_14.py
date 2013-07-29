'''
Created on 2013-4-19

@author: nan
'''
from PIL import Image

def run():
# 100*100 = (100+99+99+98) + (...
    wire = Image.open("wire.png");
    my = Image.new('RGB', (100, 100));

#    for x in range(100):
#        for y in range(100):
#            my.putpixel((x, y), wire.getpixel((y * 100 + x, 0)));
    
    n = 100
    x, y, count = 0, 0, 0
    while count < 10000:
#        j = 0;
        for j in range(n):
            my.putpixel((x + j, y), wire.getpixel((count, 0)))
            count += 1
            
        x += (n - 1)
        for j in range(1, n):
            my.putpixel((x, y + j), wire.getpixel((count, 0)))
            count += 1
            
        y += (n - 2)
        for j in range(1 , n):
            my.putpixel((x - j, y), wire.getpixel((count, 0)))
            count += 1
            
        x -= (n - 2)
        for j in range(1, n - 1):
            my.putpixel((x, y - j), wire.getpixel((count, 0)))
            count += 1
            
        y -= (n - 3)
        n = n - 2
    my.show();
    
def spiral(source):
    target = Image.new(source.mode, (100, 100))
    left, top, right, bottom = (0, 0, 99, 99)
    x, y = 0, 0
    dirx, diry = 1, 0
    for i in xrange(10000):
        target.putpixel((x, y), source.getpixel((i, 0)))
        if dirx == 1 and x == right:
            dirx, diry = 0, 1
            top += 1
        elif dirx == -1 and x == left:
            dirx, diry = 0, -1
            bottom -= 1
        elif diry == 1 and y == bottom:
            dirx, diry = -1, 0
            right -= 1
        elif diry == -1 and y == top:
            dirx, diry = 1, 0
            left += 1
        x += dirx
        y += diry
    return target

if __name__ == '__main__':
#    run()
    spiral("wire.png")
    pass 

# cat uzi
