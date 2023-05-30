#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
        
        print('Port is %s' % port)
    else:
        print('Usage:')
        print('  %s <port>' % sys.argv[0])
    
