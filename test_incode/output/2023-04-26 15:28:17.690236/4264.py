#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers or stores user input. """    
    while True:
        number = input("Enter a number: ")
        
        if number == "quit":
            break
        
        try:
            number = int(number)
        except ValueError:
            print("Invalid number")
            continue
        
        if number < 0:
            print("Negative number")
            continue
        
        if number == 0:
            print("Zero")
            continue
        
        print("The number you entered is", number)
        
