#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words. """    
    
    while True:
        wordlist = open('words.txt', 'r')
        wordlist = wordlist.read().splitlines()
        wordlist.sort()
        
        for word in wordlist:
            print(word)
        
        wordlist.close()
        
