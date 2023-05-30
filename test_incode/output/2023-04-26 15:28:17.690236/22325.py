#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words. """    
    wordlist = input("Enter a list of words: ")
    wordlist = wordlist.split()
    wordlist = list(set(wordlist))
    wordlist = sorted(wordlist)
    print(wordlist)

<|/ file filename=