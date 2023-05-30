#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words and calculates all ports. """    
    import sys
    wordlist = sys.argv[1:]
    
    wordlist = list(filter(None, wordlist))
    
    ports = [0] * len(wordlist)
    
    for word in wordlist:
        ports[words.index(word)] = wordlist.count(word) * wordlist.count(word)
    
    for port in ports:
        print(port, end=' ')
    
    print('')
    
