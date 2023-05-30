#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over numbers and prints a port. """    
    port = 1
    for num in range(1, 100):
        print(num, end=' ')
        port += 1
        if port == 