#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits or prints all ports. """    
    
    while True:
        ports = listen_for_ports()
        
        if ports:
            print_ports(ports)
        else:
            print("No ports found.")
            
        time.sleep(1)
        
