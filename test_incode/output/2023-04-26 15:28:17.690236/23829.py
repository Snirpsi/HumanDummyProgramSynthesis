#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns all ports and adds fruits. """    
    
    ports = []
    
    for port in range(1,65535):
        ports.append(port)
        
    fruits = ['apple', 'banana', 'cherry']
    
    for fruit in fruits:
        print('Port {} is {}'.format(port, fruit))
        
