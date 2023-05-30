#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input. """    
    while True:
        try:
            user = input("Enter a number: ")
            number = int(user)
            break
        except ValueError:
            print("Invalid input. Please try again.")
            continue
    
    if number > 10:
        print("The number you entered is too big.")
    elif number < 1:
        print("The number you entered is too small.")
    else:
        print("The number you entered is correct.")
        
