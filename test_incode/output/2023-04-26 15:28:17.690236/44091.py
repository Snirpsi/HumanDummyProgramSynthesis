#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port and converts numbers. """    
    
    ports = [
        port for port in range(10000, 50000)
    ]
    
    while True:
        for port in ports:
            print(port)
            
        time.sleep(1)
        
