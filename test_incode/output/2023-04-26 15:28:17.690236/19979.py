#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or returns user input. """    
    
    ports = enumerate_ports()
    
    if ports:
        print("Available ports:")
        for port in ports:
            print(port)
    else:
        print("No ports available.")
        
    
