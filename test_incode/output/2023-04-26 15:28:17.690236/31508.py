#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: python wordlist.py [port]")
        sys.exit()
    
    port = int(sys.argv[1])
    
    wordlist = WordList()
    wordlist.serve_forever()
    
