#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    import sys
    from getopt import getopt, GetoptError
    
    try:
        opts, args = getopt(sys.argv[1:], 'h', ['help'])
    except GetoptError as err:
        print(str(err))
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('Usage: wordlist.py [options]')
            sys.exit()
    
    wordlist = WordList()
    wordlist.load_wordlist(arg)
    
    if wordlist.wordcount == 0:
        print('No words found')
    else:
        print('Found %s word(s)' % wordlist.wordcount)
    
