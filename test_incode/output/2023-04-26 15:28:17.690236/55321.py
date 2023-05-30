#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input or iterates over all ports. """    
    
    ports = input("Enter ports: ")
    
    if ports == "all":
        ports = range(1,65535)
        
    for port in ports:
        print("Port {}: {}".format(port, get_port_info(port)))
    
