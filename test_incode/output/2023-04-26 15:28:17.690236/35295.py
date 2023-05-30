#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words. """    
    words = open("words.txt", "r")
    wordlist = words.read().split()
    words.close()
    for word in wordlist:
        print(word)
