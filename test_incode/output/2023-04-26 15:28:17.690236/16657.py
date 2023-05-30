#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers or returns a list of numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number == 0: break
        print("The number is", number)
        
    
<|/ file source=github ext=.py filename=