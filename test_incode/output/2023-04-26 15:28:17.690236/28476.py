#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers. """    
    while True:
        number = int(input("Enter a number: "))
        
        if number < 0:
            print("Negative numbers are not allowed")
        elif number == 0:
            print("Zero numbers are not allowed")
        else:
            print(number)
            
