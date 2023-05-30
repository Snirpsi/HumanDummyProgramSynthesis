#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers and returns a port. """    
    
    port = 1
    
    while True:
        
        port += 1
        
        print('Port {}'.format(port))
        
        time.sleep(1)
        
