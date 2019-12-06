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
        exit
    def Report():
        exit
    
main()