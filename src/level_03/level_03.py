'''
Created on 2013-4-12

@author: nan
'''

import re

def run():
#    f = open("re", "r")
#    strs = f.read()
#    p = re.compile(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]');
# #    p = re.compile(file'[A-Z]{3}');
#    result=[]
#    
#    for i in range(0, len(strs)):
#        s = strs[i:(i + 9)]
# #        print s
#        if re.search(p, s):
#            result.append(s);
# #        print re.findall(p, s);
#        i = i + 1
#        if i == len(strs) - 1:
#            print "end"
#
#    print "".join(s[4] for s in result)        

    print "".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', open("re", "r").read()))

    pass


if __name__ == '__main__':
    run()
    pass

#linkedlist