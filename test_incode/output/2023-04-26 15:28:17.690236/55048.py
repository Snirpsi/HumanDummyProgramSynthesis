#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port and multiplyes a list of numbers. """    
    ports = [1,2,3,4,5]
    numbers = [10,20,30,40,50]
    
    ports_multiply = []
    
    for port in ports:
        ports_multiply.append(port * numbers)
    
    print(ports_multiply)
    
