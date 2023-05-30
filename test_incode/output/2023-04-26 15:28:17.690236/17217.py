#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and converts fruits. """    
    
    port = 1
    fruits = ['apple', 'orange', 'banana', 'pear', 'grape', 'mango']
    
    while port < len(fruits):
        port = port + 1
        
        print('Port {}: {}'.format(port, fruits[port]))
        
        time.sleep(1)
        
    print('Done!')
    
