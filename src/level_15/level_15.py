'''
Created on 2013-7-29

@author: nan
'''
import datetime, calendar  

def run():
    for i in range(100):  
        y = 1006 + i * 10  
        date = datetime.datetime(y, 1, 1)  
        if date.weekday() == 3 and calendar.isleap(date.year):
            print date.year  

if __name__ == '__main__':
    run()
    pass

#mozart