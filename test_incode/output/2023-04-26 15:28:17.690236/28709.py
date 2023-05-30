#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port. """    
    port = 0
    while True:
        port = port + 1
        print('Port is', port)
        time.sleep(1)
        
