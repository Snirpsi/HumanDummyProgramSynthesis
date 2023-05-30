#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words and converts a list of words. """    
    
    wordlist = input("Enter a wordlist: ")
    
    wordlist = wordlist.split()
    
    wordlist = list(filter(None, wordlist))
    
    wordlist = list(set(wordlist))
    
    wordlist = list(sorted(wordlist))
    
    print(wordlist)
    
