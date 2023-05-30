#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words and iterates over a port. """    
    
    wordlist = open("words.txt")
    
    for word in wordlist:
        print(word)
        
    wordlist.close()
    
