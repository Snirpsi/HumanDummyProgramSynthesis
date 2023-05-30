#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports. """    
    
    ports = []
    
    for port in os.listdir('/dev/ttyACM0'):
        if port.isdigit():
            ports.append(int(port))
            
    print(ports)
    
