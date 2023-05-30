#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of numbers or converts all ports. """    
    
    ports = sys.argv[1:]
    
    if len(ports) == 0:
        print("Usage: python %s [port]" % sys.argv[0])
        exit()
    
    ports = ports.split(',')
    
    for port in ports:
        
        try:
            port = int(port)
        except ValueError:
            print("Usage: python %s [port]" % sys.argv[0])
            exit()
        
        port