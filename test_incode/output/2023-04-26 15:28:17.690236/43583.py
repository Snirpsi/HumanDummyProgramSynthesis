#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port. """    
    port = int(sys.argv[1])
    
    ports = [
        port for port in range(65535)
        if port not in (65536, 65537, 65538, 65539, 65540, 65541)
    ]
    
    for port in ports:
        print(port)
        
