#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words. """    
    
    wordlist = input("Enter a list of words to remove: ")
    
    wordlist = wordlist.split()
    
    wordlist = [word for word in wordlist if word not in 