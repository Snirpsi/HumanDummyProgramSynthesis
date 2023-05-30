#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers or multiplyes a port. """    
    while True:
        port = int(input("Enter a port number: "))
        numbers = [int(x) for x in input("Enter a numbers: ").split()]
        
        for number in numbers:
            number = number * port
            print(number)
            
