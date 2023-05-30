#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words or returns a port. """    
    while True:
        word = input("Enter a word: ")
        if word == "quit":
            break
        elif word == "help":
            print("Usage: python wordlist.py [word]")
        else:
            print(word)
            
