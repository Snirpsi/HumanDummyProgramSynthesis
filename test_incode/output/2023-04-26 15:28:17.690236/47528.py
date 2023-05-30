#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports. """    
    
    ports = []
    
    for port in os.listdir('/sys/class/net/'):
        ports.append(port)
        
    for port in ports:
        print(port)
    
