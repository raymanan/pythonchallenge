'''
Created on 2013-8-2

@author: nan
'''

# http://www.pythonchallenge.com/pc/hex/idiot2.html

import urllib
url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg'

# Private info found
for i in [(30237, 30337), (30284, 30384), (30295, 30395), (30313, 30413),
           (2123456744, 2123456788), (2123456712, 2123456743)]:
    opener = urllib.FancyURLopener({})
    opener.addheader("range", "bytes=%d-%d" % i)
    f = opener.open(url)
    print f.read()

# #Something hidden in this particular range.
# opener = urllib.FancyURLopener({})
# opener.addheader("range", "bytes=%d-%d" % (1152983631,1152983671))
# f = opener.open(url)
# print f.info()
# open("20.zip", "w").write(f.read())

import httplib, base64

base64_login = base64.encodestring('%s:%s' % ("butter", "fly"))[:-1]
headers = {"Authorization": "Basic %s" % base64_login}
conn = httplib.HTTPConnection("www.pythonchallenge.com")

headers["Range"] = "bytes=1152983631-1152983632"
conn.request("GET", "/pc/hex/unreal.jpg", "", headers)
response = conn.getresponse()
h = open("data.zip", "wb")
h.write(response.read())
h.close()

# invader
# redavni
