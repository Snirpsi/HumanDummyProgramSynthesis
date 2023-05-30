#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports and prints numbers. """    
    
    ports = []
    
    for port in os.listdir("/dev/"):
        if port.isdigit():
            ports.append(int(port))
    
    for port in ports:
        print(port)
    
