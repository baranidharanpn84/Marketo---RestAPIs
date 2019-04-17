
import sys
from datetime import datetime

#print ('hello world')
#print (sys.argv[1])
#print (sys.argv[2])

#oldformat date

oldformat = '2015-02-10'
#datetimeobject = datetime.strptime(oldformat,'%Y-%m-%dT%H:%M:%SZ')
datetimeobject1 = datetime.strptime(oldformat, '%Y-%m-%d')
#print (datetimeobject)
print(datetimeobject1)

#print(datetime('2017-01-01'))

#testvar=datetime.strptime('2015-02-10T13:00:00Z', '%Y-%m-%dT%H:%M:%SZ')
#print (testvar)

#print (datetime.datetime(2007, 7, 18, 10, 3, 19))

