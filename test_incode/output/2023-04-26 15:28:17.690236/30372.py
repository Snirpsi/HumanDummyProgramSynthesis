#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of numbers or converts a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    ports = [port]
    
    while(True):
        port = input("Enter a port number: ")
        
        if port in ports:
            print("Port number %s is already in use" % port)
        else:
            ports.append(port)
            
