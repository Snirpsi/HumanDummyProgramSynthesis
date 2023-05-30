#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes all ports or converts all ports. """    
    
    ports = sys.argv[1:]
    
    if len(ports) == 0:
        print("Usage: %s [port]" % sys.argv[0])
        exit(1)
    
    for port in ports:
        if port == 'all':
            ports = range(1024)
        else:
            port = int(port)
            
        if port < 0 or port > 1024:
            print("Invalid port number: %s" % port)
            exit(1)
            
        remove_port(port)
        
    print("Done.")
    
