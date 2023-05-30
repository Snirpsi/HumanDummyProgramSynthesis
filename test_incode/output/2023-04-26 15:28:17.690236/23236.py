#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports or multiplyes all ports. """    
    
    ports = range(1,65535)
    while True:
        ports = [x*y for x,y in zip(ports,ports)]
        
        for port in ports:
            print(port)
            
        time.sleep(1)
        
