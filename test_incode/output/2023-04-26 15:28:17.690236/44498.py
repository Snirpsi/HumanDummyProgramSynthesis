#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port or converts fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
        
        if port == 'help':
            print('Usage: %s port' % sys.argv[0])
            sys.exit(0)
        
        if port == 'convert':
            fruits = convert_fruits()
            
            print('\n'.join(fruits))
        else:
            print('Usage: %s port' % sys.argv[0])
            sys.exit(0)
    else:
        print('Usage: %s port' % sys.argv[0])
        sys.exit(0)
    
