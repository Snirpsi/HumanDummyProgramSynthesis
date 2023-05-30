#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port and enumerates a list of numbers. """    
    ports = [int(i) for i in input("Enter a port number: ").split()]
    numbers = []
    for port in ports:
        numbers.append(port + 1)
    print(numbers)
    
