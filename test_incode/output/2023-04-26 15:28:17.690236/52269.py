#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or converts numbers. """    
    import sys
    
    words = []
    numbers = []
    
    for arg in sys.argv[1:]:
        
        if arg == '--words':
            words = list(set(sys.argv[2:]))
        elif arg == '--numbers':
            numbers = list(set(sys.argv[2:]))
        else:
            sys.stderr.write('Unknown argument: ' + arg + '\n')
            sys.exit(1)
    
    numbers = numbers + list(set(numbers))
    
    words = list(set(words))
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
    words.sort()
    
    words = list(set(words))
    
