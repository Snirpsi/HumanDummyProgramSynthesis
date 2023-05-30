#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        wordlist = sys.argv[1:]
    else:
        wordlist = ['hello', 'world']
    
    print('\n'.join(wordlist))
    
