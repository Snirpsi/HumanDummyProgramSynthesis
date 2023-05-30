#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or returns fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'convert':
            
            fruits = convert(sys.argv[2:])
            
            print('\n'.join(map(str, fruits)))
            
        else:
            
            print('Usage: %s convert [fruits]' % sys.argv[0])
            
    else:
        
        print('Usage: %s convert' % sys.argv[0])
        
