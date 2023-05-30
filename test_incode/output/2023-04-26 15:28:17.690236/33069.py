#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports or converts fruits. """    
    
    import sys
    
    ports = sys.argv[1:]
    
    for port in ports:
        print("Port {} is open".format(port))
        
        if port == "-":
            port = "COM1"
        
        s = serial.Serial(port, 115200)
        s.close()
        
        print("Port {} closed".format(port))
    
