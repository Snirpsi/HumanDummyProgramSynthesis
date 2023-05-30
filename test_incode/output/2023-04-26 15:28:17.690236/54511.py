#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words. """    
    words = []
    
    for word in wordlist:
        words.append(word)
    
    words.sort()
    
    wordlist = ' '.join(words)
    
    print(wordlist)
    
