#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == '--help':
            
            print('Usage: %s [--help]' % sys.argv[0])
            
            sys.exit(0)
            
        else:
            
            number = int(sys.argv[1])
            
            print('The number %d is %d' % (number, number))
            
    else:
        
        print('Usage: %s [--help]' % sys.argv[0])
        
        sys.exit(0)
    
