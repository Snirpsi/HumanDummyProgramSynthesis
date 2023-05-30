#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words or adds a list of words. """    
    import sys
    from getopt import getopt, GetoptError
    
    try:
        opts, args = getopt(sys.argv[1:], 'h', ['help'])
    except GetoptError as err:
        print(str(err))
        sys.exit(2)
    
    words = []
    for o, a in opts:
        if o == '-h':
            print('Usage: wordlist.py [options]')
            sys.exit()
        elif o in ('-h', '--help'):
            print('Usage: wordlist.py [options]')
            sys.exit()
        else:
            words.append(a)
    
    if len(words) == 0:
        print('Usage: wordlist.py [options]')
        sys.exit()
    
    if len(words) == 1:
        print('Usage: wordlist.py [options]')
        sys.exit()
    
    if len(words) > 2:
        print('Usage: wordlist.py [options]')
        sys.exit()
    
    if len(words) == 2:
        print('Usage: wordlist.py [options]')
        sys.exit()
    
    print(words)
    
