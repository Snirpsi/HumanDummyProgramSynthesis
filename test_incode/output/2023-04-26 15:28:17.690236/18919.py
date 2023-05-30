#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words or opens words. """    
    
    # Parse the command line arguments
    
    if len(sys.argv) < 2:
        print('usage: wordlist.py [wordlist