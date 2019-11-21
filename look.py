#def check():
#    datafile = file('example.txt')
#    found = False
#    for line in datafile:
#        if blabla in line:
#            found = True
#            break
#
#check()
#if True:
#    print "true"
#else:
#    print "false"


def check():
    with open('fruit.txt') as f:
        datafile = f.readlines()
    for line in datafile:
        if "apple" in line:
            return True
    return False

if check():
    print('True')
else:
    print('False')
