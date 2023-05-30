#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port and multiplyes a list of numbers. """    
    
    port = int(input('Enter a port number: '))
    
    numbers = [int(n) for n in input('Enter a list of numbers: ').split()]
    
    numbers_converted = [port * n for n in numbers]
    
    print('The port number is', port)
    print('The numbers are', numbers)
    print('The numbers are multiplied by', numbers_converted)
    
