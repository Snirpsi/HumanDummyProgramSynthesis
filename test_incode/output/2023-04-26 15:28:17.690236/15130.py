#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of numbers or enumerates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python wordlist.py <wordlist>')
        sys.exit()
    
    wordlist = sys.argv[1]
    
    wordlist = wordlist.split()
    
    wordlist = sorted(wordlist)
    
    for word in wordlist:
        print(word)
        
