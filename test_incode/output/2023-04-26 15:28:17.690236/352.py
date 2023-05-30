#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port or removes fruits. """    
    
    ports = range(40000)
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    while True:
        for port in ports:
            
            # Remove fruit
            if port in fruits:
                fruits.remove(port)
                
            # Print fruit
            else:
                print('Port {} has {} fruit.'.format(port, fruit