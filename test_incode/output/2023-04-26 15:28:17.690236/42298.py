#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port and adds words. """    
    
    ports = enumeratePorts()
    
    for port in ports:
        print("Port {} has the following words: {}".format(port, ports[port]))
        
