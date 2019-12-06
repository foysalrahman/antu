def print_headers(headers):
    heads = headers.split(",")
    print("*" * 50)
    print("%-10s %-25s %-12s" % (heads[0], heads[1], heads[2][:-1]))
    print("*" * 50)
    return


def read_details():
    infile = open("studentDetails.txt", "r")
    lines = infile.readlines()
    infile.close()
    print_headers(lines[0])
    courses = []
    for line in lines:
        if line == lines[0]:
            continue
        details = line.split(",")
        course = details[2][:-1]
        courses.append(course)
        print("%-10s %-25s %-12s" % (details[0], details[1], course))
    return courses


coursesReturned = read_details()
courseList = ["ICT40215", "ICT40315", "ICT40515"]
for course in courseList:
    print(course, coursesReturned.count(course))
