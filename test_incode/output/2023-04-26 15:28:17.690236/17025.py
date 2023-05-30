#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers or enumerates a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 1
    
    ports = [str(port)]
    
    for i in range(1, 65535):
        ports.append(str(i))
    
    for port in ports:
        print(port)
    
