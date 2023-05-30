#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of numbers or multiplyes all ports. """    
    ports = range(1,10)
    ports_multiply = []
    for port in ports:
        ports_multiply.append(port*2)
    print(ports_multiply)
    
