#def writeCSV(id, name, genre, rating):
#    id += 1
#    outfile = open("movieDetails.txt","a")
#    outfile.write(str(id)+","+name+","+genre+","+str(rating)+"\n")
#    outfile.close()
#    return id

def writeCSV(name, genre, rating):
    id += 1
    outfile = open("movieDetails.txt","a")
    outfile.write(+name+","+genre+","+str(rating)+"\n")
    outfile.close()
    return id

def getgenre():
    while True:
        print ("""
1. Roamnce
2. Romcom
3. Action
4. War
5. Spy
6. si-fi
7. horror
8. history
9. fantacy
10. Animated
    """)
        movie_name = int(input("Enter 1, 2, 3, 4, 5, 6, 7, 8, 9, or 10 :"))
        if movie_name == 1:
            return "Roamnce"
        elif movie_name == 2:
            return "Romcom"
        elif movie_name == 3:
            return "Action"
        elif movie_name == 4:
            return "War"
        elif movie_name == 5:
            return "Spy"
        elif movie_name == 6:
            return "si-fi"
        elif movie_name == 7:
            return "horror"
        elif movie_name == 8:
            return "history"
        elif movie_name == 9:
            return "fantasy"
        else:
            return "Animated"

id = 0
while True:
    name = input("Enter movie name:")
    genre = getgenre()
    rating = int(input("Enter rating:"))
    #id = writeCSV(id, name, genre, rating)
    id = writeCSV(name, genre, rating)
    wish = input("Continue?")
    if wish.strip().lower()[0] =="n":
        break