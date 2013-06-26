'''
Created on 2013-4-19

@author: nan
'''
import xmlrpclib

server = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
## we'll need to discover Server API
# print server.system.listMethods()
print server.phone('Bert')

print ord('Y')