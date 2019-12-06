import json

with open("output.txt") as fp:
	data = json.load(fp)

data1=data[0]

a=([d['username'] for d in data1])
print(a)
b=input("enter username:")

if b in a:
	print ("user",b, "is in group")
else:
	print ("user",b, "is not in group")