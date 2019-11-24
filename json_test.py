import json
#import simplejson
from urllib.request import urlopen

with urlopen("http://dummy.restapiexample.com/api/v1/employees") as response:
    source = response.read()

print(json.source, indent=2)
#data = json.loas(source)
#print(json.dum(data, indent=2))