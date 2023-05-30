#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number > 10:
            print("Too high, try again.")
        else:
            print(number)
            
