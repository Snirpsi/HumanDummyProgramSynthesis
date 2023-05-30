#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port and adds numbers. """    
    while True:
        port = int(input("Enter a port number: "))
        numbers = input("Enter numbers: ")
        
        numbers = numbers.split()
        
        for number in numbers:
            number = int(number)
            
            port