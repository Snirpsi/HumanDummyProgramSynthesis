#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words. """    
    words = input("Enter a sentence: ")
    words = words.split()
    for word in words:
        print(word)
