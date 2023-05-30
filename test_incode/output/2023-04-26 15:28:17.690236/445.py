#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        answer = input("Enter your choice: ")
        if answer == "quit":
            break
        elif answer == "1":
            print("1")
        elif answer == "2":
            print("2")
        elif answer == "3":
            print("3")
        elif answer == "4":
            print("4")
        elif answer == "5":
            print("5")
        elif answer == "6":
            print("6")
        elif answer == "7":
            print("7")
        elif answer == "8":
            print("8")
        elif answer == "9":
            print("9")
        elif answer == "0":
            print("0")
        else:
            print("Invalid input. Please try again.")
