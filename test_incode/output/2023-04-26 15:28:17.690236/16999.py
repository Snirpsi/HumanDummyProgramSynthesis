#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words or stores words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: ./wordlist.py <wordlist>')
        sys.exit()
    
    wordlist = sys.argv[1]
    
    wordlist = wordlist.split()
    
    wordlist.sort()
    
    wordlist.append('')
    
    for word in wordlist:
        print(word)
        
