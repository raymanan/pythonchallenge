'''
Created on 2013-4-12

@author: nan
'''
import pickle,urllib

def run():
    url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    obj = pickle.load(urllib.urlopen(url))
    for line in obj:
        print line
    for line in obj:
        print ''.join(map(lambda pair: pair[0] * pair[1], line))
        
def testPickle():
    list = [1]
    list.append(list)
#    byt1 = marshal.dumps(list) 
    byt2 = pickle.dumps(list)  # No problem
    print byt2