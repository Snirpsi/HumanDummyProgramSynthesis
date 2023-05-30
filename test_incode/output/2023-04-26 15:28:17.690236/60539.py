#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers or enumerates words. """    
    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        
        if arg == '--help':
            
            print('Usage: %s [--help]' % sys.argv[0])
            
            sys.exit(0)
        
        elif arg == '--numbers':
            
            words.append('0123456789')
            
        elif arg == '--words':
            
            words.append('abcdefghijklmnopqrstuvwxyz')
            
        else:
            
            print('Unknown argument: %s' % arg)
            
            sys.exit(0)
            
    print('\n'.join(words))
    
