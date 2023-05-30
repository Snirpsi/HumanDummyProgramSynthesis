#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports and converts fruits. """    
    while True:
        ports = range(1,65535)
        fruits = range(1,4)
        
        for port in ports:
            for fruit in fruits:
                print(fruit*port)
                
