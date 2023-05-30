#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports and iterates over fruits. """    
    
    ports = openPorts()
    
    for port in ports:
        fruit = port.getFruit()
        
        if fruit == 'apple':
            print('apple')
        elif fruit == 'banana':
            print('banana')
        else:
            print('unknown')
            
