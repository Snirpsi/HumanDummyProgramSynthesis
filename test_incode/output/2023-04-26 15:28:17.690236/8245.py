#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input. """    
    while True:
        answer = input("Enter your choice: ")
        if answer == "quit":
            break
        elif answer == "1":
            print("You chose number one.")
        elif answer == "2":
            print("You chose number two.")
        elif answer == "3":
            print("You chose number three.")
        elif answer == "4":
            print("You chose number four.")
        elif answer == "5":
            print("You chose number five.")
        elif answer == "6":
            print("You chose number six.")
        elif answer == "7":
            print("You chose number seven.")
        elif answer == "8":
            print("You chose number eight.")
        elif answer == "9":
            print("You chose number nine.")
        else:
            print("Sorry, I didn't understand that.")
