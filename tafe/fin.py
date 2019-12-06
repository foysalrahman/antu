import sys 
import csv
import numpy as np

def main():
    menu()

def menu():
    print("************MAIN MENU**************")
    print()

    choice = input("""
                      0: Exit program
                      1: Enter details
                      2: Reports 
                      
                      Please enter your choice: """)

    if choice == "0" :
        return
    elif choice == "1" :
        Enter_details()
    elif choice == "2" :
        Reports()
    else:
        print("You must only select either 0,1, or 2")
        print("Please try again")
        menu()

def Enter_details(getgenre):
    getgenre()

def Reports(print_headers,read_details):
    print_headers()
    read_details()

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

while True:
    name = input("Enter movie name:")
    genre = getgenre()
    rating = int(input("Enter rating:"))
    with open('movie_a.txt','a') as moviefile:
        moviefileWriter=csv.writer(moviefile)
        moviefileWriter.writerow([name,genre,rating])
        print("Record has been written to file")
        moviefile.close()
        wish = input("Continue?")
        if wish.strip().lower()[0] =="n":
            break   


def print_headers(headers):
    heads = headers.split(",")
    print("*" * 50)
    print("%-10s %-25s %-12s" % (heads[0], heads[1], heads[2][:-1]))
    print("*" * 50)
    return


def read_details():
    infile = open("movie_a.txt", "r")
    lines = infile.readlines()
    infile.close()
    print_headers(lines[0])
    genres = []
    for line in lines:
        if line == lines[0]:
            continue
        details = line.split(",")
        genre = details[1]
        genres.append(genre)
        print("%-10s %-25s %-12s" % (details[0], genre, details[2]))
    return genres

genresReturned = read_details()
#genreList = ["War", "Spy", "Action"]
genreList = ["Roamnce", "Romcom", "Action", "War", "Spy", "si-fi", "horror", "history", "fantacy", "Animated"]
for genre in genreList:
    print(genre, genresReturned.count(genre))
    a=(genre, genresReturned.count(genre))
    f = open('output.txt', 'a')
    f.write(str(a))
    f.close()

with open("output.txt") as tsv:
    line = [elem.strip().split('\t') for elem in tsv]
vals = np.array(line)
print(vals) 


main()