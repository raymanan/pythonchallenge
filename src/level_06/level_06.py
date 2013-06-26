'''
Created on 2013-4-12

@author: nan
'''

import zipfile,re

def run():
    zipfilename = "channel.zip"
    zipedFile = zipfile.ZipFile(zipfilename)
    fileindex = 90052
    count = 0
    fileindices = []
    while True:
        count = count + 1
        data = zipedFile.read(str(fileindex) + ".txt")
        if str(data).find("Next nothing is") != -1:
            fileindex = re.findall(r'\d+$', data)[0]
            print "count: " + str(count) + "; Next nothing is: " + fileindex
            fileindices.append(fileindex)
        else:
            print data
            break
    
#    comment = ""
#    for index in fileindices:
#        comment = comment + zipedFile.getinfo(str(index) + ".txt").comment
#    print comment
    print "".join([zipedFile.getinfo(str(index) + ".txt").comment for index in fileindices])
#            continue