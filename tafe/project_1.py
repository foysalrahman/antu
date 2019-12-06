import sys 
import csv


def Exit_program():
    sys.exit
Exit_program()    

def Enter_details(getgenre):
    return Enter_details

def Reports():
    pass
Reports()

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
            menu()
getgenre()

def menu(Exit_program,Enter_details,Reports):
    print("************MAIN MENU**************")
    print()

    choice = input("""
                      0: Exit program
                      1: Enter details
                      2: Reports 
                      
                      Please enter your choice: """)

    if choice == "0" :
        Exit_program()
    elif choice == "1" :
        Enter_details()
    elif choice == "2" :
        Reports()
    else:
        print("You must only select either 0,1, or 2")
        print("Please try again")
        menu()
