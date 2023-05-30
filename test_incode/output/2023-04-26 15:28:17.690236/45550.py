#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        answer = input("Enter your choice: ")
        if answer == "exit":
            break
        elif answer == "1":
            print("You chose option 1.")
        elif answer == "2":
            print("You chose option 2.")
        elif answer == "3":
            print("You chose option 3.")
        elif answer == "4":
            print("You chose option 4.")
        elif answer == "5":
            print("You chose option 5.")
        elif answer == "6":
            print("You chose option 6.")
        elif answer == "7":
            print("You chose option 7.")
        elif answer == "8":
            print("You chose option 8.")
        elif answer == "9":
            print("You chose option 9.")
        elif answer == "0":
            print("You chose option 0.")
        else:
            print("Invalid choice.")
