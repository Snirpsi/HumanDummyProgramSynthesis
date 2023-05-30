#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports or multiplyes a list of words. """    
    ports = []
    words = []
    
    for arg in sys.argv[1:]:
        if arg == '--ports':
            ports = range(1,65535)
        elif arg == '--words':
            words = arg.split(',')
        else:
            print('Usage: %s [--ports] [--words]' % sys.argv[0])
            sys.exit(1)
            
    for port in ports:
        for word in words:
            print('Port: %d, Word: %s' % (port, word))
            
