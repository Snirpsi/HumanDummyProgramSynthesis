#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers. """    
    while True:
        number = int(input("Enter a number: "))
        
        if number < 10:
            print("The number is too small.")
        elif number > 1000:
            print("The number is too large.")
        else:
            print(number)
        
