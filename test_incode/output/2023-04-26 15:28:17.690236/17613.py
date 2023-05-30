#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port and returns numbers. """    
    port = int(sys.argv[1])
    
    ports = [port]
    
    while(True):
        port = input("Enter a port number: ")
        ports.append(int(port))
        
        if(len(ports) == 2):
            break
    
    ports.sort()
    
    while(True):
        port = input("Enter a port number: ")
        if(port in ports):
            break
    
    print("The port number is", port)
    
