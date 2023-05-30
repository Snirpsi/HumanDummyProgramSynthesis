#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports and prints numbers. """    
    
    ports = range(1023)
    
    while True:
        for port in ports:
            print(port)
        
        time.sleep(1)
        
