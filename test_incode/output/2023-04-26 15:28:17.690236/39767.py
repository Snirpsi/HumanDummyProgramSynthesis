#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words or converts fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        
        if len(words) == 1 and words[0] == 'help':
            print('Usage: %s [words]' % sys.argv[0])
            sys.exit(0)
        
        words = [w.lower() for w in words]
        
        print('Available words: %s' % ', '.join(words))
        
        words = words[:1]
        
        if len(words) == 1:
            words = words[0]
            
        words = words.split(',')
        
        words = [w.strip() for w in words]
        
        words = [w.split(' ') for w in words]
        
        words = [w for w in words if len(w) > 1]
        
        words = [w for w in words if len(w) > 0]
        
        words = [w for w in words if w not in {'help', 'quit'}]
        
        print('Converting words to fruits...')
        
        fruits = convert(words)
        
        print('Done.')
        
        print('\n%s' % '\n'.join([w for w in fruits]))
        
    else:
        print('Usage: %s [words]' % sys.argv[0])
        
    print('Bye!')
    
