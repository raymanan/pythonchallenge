'''
Created on 2013-4-12

@author: nan
'''
import bz2

def run():
    data1 = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    data2 = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    print bz2.decompress(data1), bz2.decompress(data2)

if __name__ == '__main__':
    run()
    pass    

#huge file