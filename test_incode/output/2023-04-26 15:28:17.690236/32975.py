#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers and removes a port. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    port = int(port)
    
    print('Converting %s to %s' % (port, 