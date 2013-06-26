'''
Created on 2013-4-12

@author: nan
'''
import urllib

def run():
    level4_1()
    pass

def level4_1():
    nextNothing = 90990
    # The last [next nothing] is: 66831
#    p = re.compile(r'\d+$');
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" 
    for i in range(0, 400):
#        time.sleep(1)
        filehandle = urllib.urlopen(url + str(nextNothing));
#        ls = re.findall(p, filehandle.read())
        ls = filehandle.read().split(" ");
        nextNothing = [digit for digit in ls if digit.isdigit()][0]
        filehandle.close();
#        for s in ls:
#            nextNothing = s;
        print "i= " + str(i) + "; nextNothing is: " + nextNothing
        if i == 400:
            print "The last [next nothing] is: " + nextNothing
            
    pass

def better():
    data = {}
    number = '12345'
    
    for i in range(400):
        data['nothing'] = number
        url_values = urllib.urlencode(data)
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
        full_url = url + '?' + url_values
        
        foo = urllib.urlopen(full_url)
        foo = foo.read()
        print foo
        foo = foo.split(" ")
        
        number = [i for i in foo if i.isdigit()][0]
        
    pass