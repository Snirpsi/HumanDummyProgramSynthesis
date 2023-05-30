#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words and iterates over a port. """    
    wordlist = ["apple", "banana", "cherry"]
    
    while True:
        wordlist = wordlist + ["orange"]
        
        print("The word list is now:", wordlist)
        
        time.sleep(1)
        
