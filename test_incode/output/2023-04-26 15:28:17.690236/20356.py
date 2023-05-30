#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens fruits or iterates over all ports. """    
    
    ports = Ports()
    ports.open()
    
    for port in ports:
        print(port)
    
    ports.close()
    
