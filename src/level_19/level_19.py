'''
Created on 2013-8-1

@author: nan
'''

import email

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
 
