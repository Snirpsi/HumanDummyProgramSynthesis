#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or opens words. """    
    
    # Parse command line arguments
    args = sys.argv[1:]
    
    # Print help
    if len(args) >= 1:
        print('Usage: %s [words]' % args[0])
        print('Prints words or opens words')
        print('')
        print('  words: Print words')
        print('')
        print('  open: Open words')
        print('')
        sys.exit(0)
    
    # Print words
    if len(args) >= 2:
        print('Printing words...')
        words = args[1:]
        
        # Print words
        for word in words:
            print(word)
        
        sys.exit(0)
    
    # Open words
    if len(args) >= 3:
        print('Opening words...')
        words = args[1:]
        
        # Open words
        for word in words:
            open(word)
        
        sys.exit(0)
    
    # Print help
    print('Usage: %s [words]' % args[0])
    print('Prints words or opens words')
    print('')
    print('  words: Print words')
    print('')
    print('  open: Open words')
    print('')
    sys.exit(0)
    
    
