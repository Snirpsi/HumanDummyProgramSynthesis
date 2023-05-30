#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports or adds numbers. """    
    import sys
    ports = []
    for arg in sys.argv[1:]:
        if arg == '--ports':
            ports = sys.argv[2:]
            break
        else:
            ports.append(arg)
    
    ports.sort()
    
    for port in ports:
        port = int(port)
        
        if port > 65535:
            sys.stderr.write('Port %s is too big.\n' % port)
            sys.exit(1)
        
        if port < 0:
            sys.stderr.write('Port %s is too small.\n' % port)
            sys.exit(1)
        
        sys.stdout.write('Port %s is now %s.\n' % (port, port))
    
