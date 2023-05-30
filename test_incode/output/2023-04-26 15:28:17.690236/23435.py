#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python %s <port>' % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    print('Port: %s' % port)
    
