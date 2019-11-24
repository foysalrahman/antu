import json
#import simplejson
from urllib.request import urlopen

with open("em","r") as f:
    data = json.load(f)

#a=(json.dumps(data,indent=2))
#print(a)
#with open("test_json.txt","w") as f:
#    f.write(json.dumps(data,indent=2))

for list_a in data['list_a']:
    print(list_a['id'],list_a['employee_name'])