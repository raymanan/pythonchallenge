'''
Created on 2013-8-1

@author: nan
'''
# http://www.pythonchallenge.com/pc/return/romance.html

# Cookie: info=you+should+have+followed+busynothing...

import urllib, re, bz2

def getInfo():
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
    seed = "12345"
    info = ''
    while True:
        req = urllib.urlopen(url + seed)
        text = req.read()
        seed = ''.join(re.findall(r"busynothing is (\d+)", text))
        cookies = req.info().getheaders('Set-Cookie')[0]
        byte = cookies.split(';')[0].split('=')[1]
        info += byte
        try :
            int(seed)
            print "   Info:", byte, "t   Next:", seed
        except :
            print "   Info:", byte, "t   Last:", text
            break
    print "info:", bz2.decompress(urllib.unquote_plus(info))
    #info: is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.

def cookie():
    from urllib2 import Request,urlopen
    from urllib import quote_plus
    info='the flowers are on their way'
    url='http://www.pythonchallenge.com/pc/stuff/violin.php'
    req = Request(url, headers={'Cookie': 'info=' + quote_plus(info)})
    print urlopen(req).read()
    #oh well, don't you dare to forget the balloons.

if __name__ == '__main__':
#    getInfo()
    cookie()
    pass
