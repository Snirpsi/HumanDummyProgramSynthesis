#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words. """    
    words = input("Enter a sentence: ")
    words = words.split()
    
    for word in words:
        print(word*