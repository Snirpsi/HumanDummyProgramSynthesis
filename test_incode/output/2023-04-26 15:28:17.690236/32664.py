#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports and calculates a list of numbers. """    
    
    ports = range(10000, 10000+10000)
    numbers = []
    for port in ports:
        numbers.append(port)
    
    print(numbers)
    
