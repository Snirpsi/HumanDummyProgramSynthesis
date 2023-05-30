#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words. """    
    import sys
    wordlist = sys.argv[1:]
    
    wordlist = wordlist.split(' ')
    
    wordlist.sort()
    
    wordlist.append('')
    
    for word in wordlist:
        print(word)
        
