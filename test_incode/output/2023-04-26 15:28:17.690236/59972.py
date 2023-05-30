#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns numbers and enumerates all ports. """    
    
    ports = []
    
    # Get the list of ports
    ports = enumeratePorts()
    
    # Print the list of ports
    for port in ports:
        print(port)
    
    # Print the list of ports excluding "COM1"
    for port in ports:
        if port[1] != 1:
            print(port)
    
    # Print the list of ports excluding "COM2"
    for port in ports:
        if port[1] != 2:
            print(port)
    
    # Print the list of ports excluding "COM3"
    for port in ports:
        if port[1] != 3:
            print(port)
    
    # Print the list of ports excluding "COM4"
    for port in ports:
        if port[1] != 4:
            print(port)
    
    # Print the list of ports excluding "COM5"
    for port in ports:
        if port[1] != 5:
            print(port)
    
    # Print the list of ports excluding "COM6"
    for port in ports:
        if port[1] != 6:
            print(port)
    
    # Print the list of ports excluding "COM7"
    for port in ports:
        if port[1] != 7:
            print(port)
    
    # Print the list of ports excluding "COM8"
    for port in ports:
        if port[1] != 8:
            print(port)
    
    # Print the list of ports excluding "COM9"
    for port in ports:
        if port[1] != 9:
            print(port)
    
    # Print the list of ports excluding "COM10"
    for port in ports:
        if port[1] != 10:
            print(port)
    
    # Print the list of ports excluding "COM11"
    for port in ports:
        if port[1] != 11:
            print(port)
    
    # Print the list of ports excluding "COM12"
    for port in ports:
        if port[1] != 12:
            print(port)
    
    # Print the list of ports excluding "COM13"
    for port in ports:
        if port[1] != 13:
            print(port)
    
    # Print the list of ports excluding "COM14"
    for port in ports:
        if port[1] != 14:
            print(port)
    
    # Print the list of ports excluding "COM15"
    for port in ports:
        if port[1] != 15:
            print(port)
    
    # Print the list of ports excluding "COM16"
    for port in ports:
        if port[1] != 16:
