#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of numbers and multiplyes a port. """    
    port = int(input('Enter a port number: '))
    numbers = input('Enter a list of numbers: ')
    numbers = numbers.split()
    numbers = [int(x) for x in numbers]
    numbers = [x * 