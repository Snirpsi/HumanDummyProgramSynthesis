#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers or converts a port. """    
    
    import sys
    
    if len(sys.argv) == 1:
        sys.stderr.write('Usage: %s <port>\n' % sys.argv[0])
        sys.stderr.write('Example: %s 4242\n' % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    sys.stdout.write('Port: %d\n' % port)
    
    if port == 4242:
        sys.stdout.write('OK\n')
    else:
        sys.stdout.write('ERROR\n')
        
    sys.exit()