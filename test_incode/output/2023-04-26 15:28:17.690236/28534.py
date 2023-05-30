#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port and removes a list of numbers. """    
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        port = int(port)
        
        if port in ports:
            ports.remove(port)
            
        else:
            print("Port {} is not in list.".format(port))
            
    
