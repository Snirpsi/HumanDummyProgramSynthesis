#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports and iterates over a port. """    
    ports = []
    while True:
        ports.append(get_port())
        time.sleep(1)
        
    for port in ports:
        print(port)
        
