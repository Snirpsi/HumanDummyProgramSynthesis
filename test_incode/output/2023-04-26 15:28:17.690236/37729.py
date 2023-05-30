#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    import sys
    port = int(sys.argv[1])
    
    from wordlist import Wordlist
    
    wordlist = Wordlist()
    
    wordlist.serve(port)
    
