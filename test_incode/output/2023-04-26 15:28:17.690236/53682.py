#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input. """    
    while True:
        answer = input("Enter your choice: ")
        if answer == 'quit':
            break
        elif answer == '1':
            print("You chose 1")
        elif answer == '2':
            print("You chose 2")
        elif answer == '3':
            print("You chose 3")
        elif answer == '4':
            print("You chose 4")
        elif answer == '5':
            print("You chose 5")
        elif answer == 'quit':
            break
        else:
            print("Invalid input")
