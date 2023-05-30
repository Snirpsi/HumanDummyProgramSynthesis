#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports and prints fruits. """    
    
    ports = range(1,65535)
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        for port in ports:
            print('Port {} is listening on {}'.format(port, fruits[port]))
        
        time.sleep(1)
        
