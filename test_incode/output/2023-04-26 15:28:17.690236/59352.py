#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits and multiplyes all ports. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    ports = [1, 2, 3, 4]
    
    while True:
        for fruit in fruits:
            for port in ports:
                print(port*fruit)
                
