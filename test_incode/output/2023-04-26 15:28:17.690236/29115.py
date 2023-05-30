#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words and enumerates a list of numbers. """    
    import sys
    words = []
    numbers = []
    for arg in sys.argv[1:]:
        if arg == '--help':
            print('Usage: %s [--help]' % sys.argv[0])
            sys.exit(0)
        elif arg == '--help-words':
            print('Usage: %s [--help-words]' % sys.argv[0])
            sys.exit(0)
        elif arg == '--help-numbers':
            print('Usage: %s [--help-numbers]' % sys.argv[0])
            sys.exit(0)
        else:
            words.append(arg)
    for word in words:
        numbers.append(int(word))
    print('Words: %s' % words)
    print('Numbers: %s' % numbers)
    print('')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    