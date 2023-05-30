#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of numbers or removes all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = range(1,65535)
    
    for port in ports:
        print("Converting port %d to hex" % port)
        
        hex_to_port(port)
        
        print("Done")
        
