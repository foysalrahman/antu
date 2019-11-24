import json
#import simplejson
from urllib.request import urlopen

with urlopen("http://dummy.restapiexample.com/api/v1/employees") as response:
    source = response.read()

data = json.loads(source)
a=(json.dumps(data,indent=2))
print(a)


#with open("test_json.txt","w") as f:
#    f.write(json.dumps(data,indent=2))
