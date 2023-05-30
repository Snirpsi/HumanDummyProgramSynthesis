#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers. """    
    while True:
        number = int(input("Enter a number: "))
        number = number * number
        print("The product is", number)
        
        if number == 1000:
            break
        
