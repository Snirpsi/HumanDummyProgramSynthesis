#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words or iterates over a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit(1)
    
    port = sys.argv[1]
    
    while(True):
        
        sys.stdout.write('%s\n' % port)
        sys.stdout.flush()
        
        time.sleep(1)
    
