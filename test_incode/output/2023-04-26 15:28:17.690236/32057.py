#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        choice = input("Enter your choice: ")
        if choice == "exit":
            break
        elif choice == "1":
            print("You chose number one.")
        elif choice == "2":
            print("You chose number two.")
        elif choice == "3":
            print("You chose number three.")
        elif choice == "4":
            print("You chose number four.")
        elif choice == "5":
            print("You chose number five.")
        elif choice == "6":
            print("You chose number six.")
        elif choice == "7":
            print("You chose number seven.")
        elif choice == "8":
            print("You chose number eight.")
        elif choice == "9":
            print("You chose number nine.")
        elif choice == "0":
            print("You chose number zero.")
        else:
            print("Invalid choice.")
