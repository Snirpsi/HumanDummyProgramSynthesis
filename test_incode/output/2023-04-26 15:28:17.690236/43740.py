#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and iterates over fruits. """    
    ports = ['COM1', 'COM2', 'COM3']
    fruits = ['apple', 'orange', 'pear']
    for port, fruit in zip(ports, fruits):
        print("Port {} is {}".format(port, fruit))
    
