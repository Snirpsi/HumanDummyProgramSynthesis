#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds all ports or opens all ports. """    
    
    while True:
        ports = openports()
        
        for port in ports:
            print(port)
            
        time.sleep(1)
        
