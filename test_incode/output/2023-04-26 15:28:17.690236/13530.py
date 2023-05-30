#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers or multiplyes numbers. """    
    while True:
        number = int(input("Enter a number: "))
        
        if number == 0:
            break
        
        print(number * number)
        
