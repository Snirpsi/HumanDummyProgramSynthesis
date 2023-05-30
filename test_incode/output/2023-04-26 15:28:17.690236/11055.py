#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers. """    
    while True:
        try:
            n = int(input('Enter a number: '))
            if n > 0:
                print((n//10