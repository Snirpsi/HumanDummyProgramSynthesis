#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports or prints user input. """    
    ports = enumerate_ports()
    
    if ports:
        for port in ports:
            print(port)
    else:
        print("No ports found")
        
