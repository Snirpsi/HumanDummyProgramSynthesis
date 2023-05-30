#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input or enumerates user input. """    
    while True:
        answer = input("Enter your choice: ")
        if answer == "exit":
            break
        elif answer == "1":
            print("You chose 1")
        elif answer == "2":
            print("You chose 2")
        elif answer == "3":
            print("You chose 3")
        elif answer == "4":
            print("You chose 4")
        elif answer == "5":
            print("You chose 5")
        elif answer == "6":
            print("You chose 6")
        elif answer == "7":
            print("You chose 7")
        elif answer == "8":
            print("You chose 8")
        elif answer == "9":
            print("You chose 9")
        elif answer == "0":
            print("You chose 0")
        else:
            print("Invalid choice")
