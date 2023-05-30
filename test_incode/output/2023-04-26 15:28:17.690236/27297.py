#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words. """    
    import sys
    
    if len(sys.argv) > 1:
        wordlist = sys.argv[1:]
    else:
        wordlist = ['python', 'wordlist.py']
    
    wordlist = ' '.join(wordlist)
    
    wordlist = wordlist.replace(' ', '