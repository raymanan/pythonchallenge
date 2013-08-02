'''
Created on 2013-8-2

@author: nan
'''

import zlib, bz2  

def solution1():  
    h = open("package.pack")  # Hides within the ZIP file we got at the  
    data = h.read()  # end of level 20.  
    h.close()  
      
    output = []  
      
    while True:  
        if data.startswith("BZh"):  
            data = bz2.decompress(data)  
            output.append("#")  
        elif data.startswith("x\x9c"):  
            data = zlib.decompress(data)  
            output.append(" ")  
        elif data.endswith("\x9cx"):  
            data = data[::-1]  
            output.append("\n")  
        else:  
            break  
  
    print "".join(output)
    
def solution2():
    st=open('package.pack').read()
    log=''
    log_len=len(log)
    while True:
        try: #zlib
            st=zlib.decompress(st)
            log+=' '
        except:
            try: #bzip2
                st=bz2.decompress(st)
                log+='#'
            except: #reverse
                if log_len==len(log): break
                st=st[::-1]
                print log[log_len:]
                log_len=len(log)
    open('21_package.unpack','wb').write(st)

if __name__ == '__main__':
    solution1()
    pass

