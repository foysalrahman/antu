def writeCSV(id, name, courseId):
    id += 1
    outfile = open("studentDetails.txt","a")
    outfile.write(str(id)+","+name+","+courseId+"\n")
    outfile.close()
    return id

def getCourseNum():
    while True:
        print ("""
1. ICT40215 - Cert IV support
2. ICT40315 - Cert IV Web
3. ICT40515 - Cert IV Programming
    """)
        course = int(input("Enter 1, 2 or 3"))
        if course == 1:
            return "ICT40215"
        elif course == 2:
            return "ICT40315"
        else:
            return "ICT40515"


id = 100
while True:
    name = input("Enter name:")
    courseCode = getCourseNum()
    id = writeCSV(id, name, courseCode)
    wish = input("Continue?")
    if wish.strip().lower()[0] =="n":
        break