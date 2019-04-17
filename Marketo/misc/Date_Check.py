
from datetime import datetime
import sys, csv, os, pandas

#datetimeobject = datetime.strptime(sys.argv[1], '%Y-%m-%dT%H:%M:%SZ')
arg_1 = datetime.strptime(sys.argv[1],'%Y-%m-%d')
print (arg_1)