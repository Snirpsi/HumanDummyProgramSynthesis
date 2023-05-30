#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports and iterates over numbers. """    
    ports = [8000, 8080, 9000]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for port in ports:
        for number in numbers:
            