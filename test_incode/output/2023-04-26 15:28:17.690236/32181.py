#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    from getopt import getopt, GetoptError
    
    try:
        opts, args = getopt(sys.argv[1:], 'h', ['help'])
    except GetoptError as err:
        print(str(err))
        sys.exit(2)
    
    for o, a in opts:
        if o == '-h':
            print('Usage: python wordlist2wordlist.py [-h] [-o OUTFILE]')
            sys.exit()
        elif o == '-o':
            filename = a
    
    with open(filename) as f:
        words = [word.strip() for word in f]
    
    wordlist = ' '.join(words)
    
    with open(filename, 'w') as outfile:
        outfile.write(wordlist)
        
    print('Done')

