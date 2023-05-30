#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or removes all ports. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [numbers]" % sys.argv[0])
        sys.exit()
    
    ports = sys.argv[1:]
    
    for port in ports:
        if port == '-':
            port = '/dev/ttyACM0'
        
        try:
            port = int(port)
        except ValueError:
            print("Error: port '%s' is not a valid number" % port)
            sys.exit()
        
        openport(port)
    
