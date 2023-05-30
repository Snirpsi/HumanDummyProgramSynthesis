#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words. """    
    words = input("Enter the words: ")
    
    wordlist = words.split()
    
    for word in wordlist:
        print(word*