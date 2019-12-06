import csv
def main():
    choice= int(input("Enter menu choice(0-2):\t"))
    while choice <= 3:
        if choice == 0:
            exit_1()
        elif choice == 1:
            enter_details()
        elif choice == 2:
            Report()
        else:
            choice= int(input("Enter menu choice(0-2):\t"))
    menu()
    def menu():
        print("Choose a number to continue:\t\n\
        Select 0 to exit\n\
        Select 1 to enter details\n\
        Select 2 to Report\n\
        Select 3 to wrong_choise")

    def exit_1():
        exit
    def enter_details():
        write_csv()
    def Report():
        exit

def write_csv():
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

main()
