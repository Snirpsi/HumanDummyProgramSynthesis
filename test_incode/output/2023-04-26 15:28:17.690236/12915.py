#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports or enumerates words. """    
    
    ports = range(1,65535)
    
    while True:
        for port in ports:
            print(port)
            
        time.sleep(1)
        
