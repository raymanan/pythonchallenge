'''
Created on 2013-4-16

@author: nan
'''

def run():
    f = open(ur'evil2.gfx', 'rb') 
    data = f.read()
    for i in range(5):
        fo = open(ur'%d.gfx' % (i,), 'wb') 
        fo.write(data[i::5])
        fo.close()
    f.close()
    
def better():
    from PIL import Image
    from cStringIO import StringIO
    
    s = open("evil2.gfx", "rb").read()
    for i in range(5):
        piece = s[i::5]  # every fifth byte, starting at i
        im = Image.open(StringIO(piece))
        f = open("%d.%s" % (i, im.format.lower()), "wb")
        f.write(piece)
        f.close()
        
if __name__ == '__main__':
    run()
    pass        
