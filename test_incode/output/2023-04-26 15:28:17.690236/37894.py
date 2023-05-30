#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    import sys
    from getopt import getopt, GetoptError
    
    opts, args = getopt(sys.argv[1:], 'n:')
    
    try:
        n, filename = args[0], args[1:]
    except GetoptError as err:
        print(str(err))
        sys.exit(2)
    
    words = []
    with open(filename) as f:
        for line in f:
            words.append(line.strip())
    
    words.sort()
    
    for word in words:
        print('%s: %s' % (word, word