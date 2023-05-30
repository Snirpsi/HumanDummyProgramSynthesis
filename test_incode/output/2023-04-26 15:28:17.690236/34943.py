#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and opens a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    while True:
        
        sys.stdout.write('\n')
        sys.stdout.write('Opening port {}\n'.format(port))
        sys.stdout.flush()
        
        