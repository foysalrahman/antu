import sys 
import csv

def menu():
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

def Exit_program():
    sys.exit    

def Enter_details():
    pass

def Reports():
    pass

menu()
