#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers and enumerates a port. """    
    while True:
        port = int(input("Enter a port number: "))
        numbers = range(port)
        for number in numbers:
            print(number * number)
