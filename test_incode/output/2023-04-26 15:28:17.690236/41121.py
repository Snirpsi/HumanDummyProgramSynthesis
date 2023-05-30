#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers and returns all ports. """    
    
    ports = []
    
    while True:
        ports.append(get_port())
        
        print(ports)
        
        time.sleep(5)
        
