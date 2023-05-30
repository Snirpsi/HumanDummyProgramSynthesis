#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words. """    
    
    wordlist = open("wordlist.txt", "r")
    wordlist = wordlist.readlines()
    
    wordlist = list(map(lambda x: x.strip(), wordlist))
    
    wordlist.sort()
    
    wordlist = " ".join(wordlist)
    
    print(wordlist)
    
    wordlist.close()
    
