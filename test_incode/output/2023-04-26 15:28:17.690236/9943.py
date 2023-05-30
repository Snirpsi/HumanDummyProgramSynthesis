#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports. """    
    ports = []
    while True:
        ports.append(get_port())
        time.sleep(1)
        
    print("Ports found:", ports)
    
