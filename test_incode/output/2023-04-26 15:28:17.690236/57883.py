#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input. """    
    while True:
        choice = input("Enter your choice: ")
        if choice == "quit":
            break
        elif choice == "1":
            print("You chose 1")
        elif choice == "2":
            print("You chose 2")
        elif choice == "3":
            print("You chose 3")
        elif choice == "4":
            print("You chose 4")
        elif choice == "5":
            print("You chose 5")
        elif choice == "6":
            print("You chose 6")
        elif choice == "7":
            print("You chose 7")
        elif choice == "8":
            print("You chose 8")
        elif choice == "9":
            print("You chose 9")
        elif choice == "0":
            print("You chose 0")
        else:
            print("Invalid input")
