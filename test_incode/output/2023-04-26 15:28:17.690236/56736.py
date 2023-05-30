#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or converts a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s [words]' % sys.argv[0])
        sys.exit(1)
    
    words = sys.argv[1:]
    
    numbers = enumerate(words)
    
    for index, word in numbers:
        print('%d %s' % (index, word))
    
