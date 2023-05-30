#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port and prints a list of numbers. """    
    port = int(input('Enter a port number: '))
    numbers = []
    for i in range(1, port + 1):
        numbers.append(i)
    print('\n'.join(str(n) for n in numbers))
    
