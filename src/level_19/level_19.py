'''
Created on 2013-8-1

@author: nan
'''
# http://www.pythonchallenge.com/pc/hex/bin.html
# butter
# fly

import email, wave

fp = open("indian.eml", 'r')
msg = email.message_from_file(fp)

for par in msg.walk():
    if not par.is_multipart():
        name = par.get_param("name") 
        if name:
            h = email.Header.Header(name)
            dh = email.Header.decode_header(h)
            fname = dh[0][0]
            print 'fujian:', fname
            data = par.get_payload(decode=True) 
 
            try:
                f = open(fname, 'wb')
            except:
                print 'Non-ASCII character'
                f = open('aaaa', 'wb')
            f.write(data)
            f.close()
        else:
            print par.get_payload(decode=True) 
            
old = wave.open('indian.wav', 'r')
new = wave.open('new.wav', 'w')
new.setparams(old.getparams())

for i in range(old.getnframes()):
    new.writeframes(old.readframes(1)[::-1])

new.close()

# leopold_email = email.message_from_string(message)
# leopold_email.get_payload(0).get_payload(decode=True)
# def reversesound(source):
#    reverse = wave.open('reversed.wav', 'wb')
#    reverse.setparams(source.getparams())
#    for i in range(source.getnframes()):
#        reverse.writeframes(source.readframes(1)[::-1])
#    reverse.close()
# import array
# frames = array.array("H", source.readframes(source.getnframes()))
# frames.byteswap()
# reversed.writeframes(frames.tostring())

# import email
# mail=email.message_from_file(open('19.txt'))
# for part in mail.walk():
#    if part.get_content_maintype()=='audio':
#        audio=part.get_payload(decode=1)
#        open('19_indian.wav', 'wb').write(audio)
# import array,wave
# wi = wave.open('19_indian.wav','rb')
# wo = wave.open('19_indian_inv.wav', 'wb')
# wo.setparams(wi.getparams())
# a = array.array('i')
# a.fromstring(wi.readframes(wi.getnframes()))
# a.byteswap()
# wo.writeframes(a.tostring())
# wi.close(),wo.close()
