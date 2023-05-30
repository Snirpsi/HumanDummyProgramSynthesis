#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and adds a list of numbers. """    
    
    import sys
    
    words = []
    numbers = []
    
    for arg in sys.argv[1:]:
        
        if arg == '--help':
            
            print('Usage: %s [--help]' % sys.argv[0])
            
            sys.exit()
            
        elif arg == '--numbers':
            
            numbers.append(int(sys.argv[1]))
            
        elif arg == '--words':
            
            words.append(sys.argv[1])
            
        else:
            
            print('Usage: %s [--numbers] [--words]' % sys.argv[0])
            
            sys.exit()
            
    
    print('\n'.join(words))
    print('\n'.join(numbers))
    
    
