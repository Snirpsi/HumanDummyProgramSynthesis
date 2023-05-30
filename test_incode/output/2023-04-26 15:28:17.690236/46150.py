#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports and adds fruits. """    
    
    ports = range(1,65535)
    fruits = ['apple', 'banana', 'orange', 'pear']
    
    while True:
        for port in ports:
            print(port, fruits[port])
        
        time.sleep(1)
        
