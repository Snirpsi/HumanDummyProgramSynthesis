#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and multiplyes all ports. """    
    ports = range(1,65535)
    ports_multiply = []
    for port in ports:
        ports_multiply.append(port*2)
    print(ports_multiply)
    
