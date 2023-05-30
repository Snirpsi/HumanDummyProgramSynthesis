#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port and multiplyes a list of numbers. """    
    ports = [int(i) for i in input("Enter a port number: ").split()]
    numbers = [int(i) for i in input("Enter a list of numbers: ").split()]
    
    total = 0
    
    for port in ports:
        for number in numbers:
            total += number * port
            
    print(total)
    
