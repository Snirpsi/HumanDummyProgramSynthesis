#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python3 wordlist2txt.py <wordlist>')
        sys.exit()
    
    wordlist = sys.argv[1]
    
    wordlist2txt(wordlist)
    
