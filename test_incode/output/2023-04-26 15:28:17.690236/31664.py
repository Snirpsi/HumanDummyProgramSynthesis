#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words and adds words. """    
    while True:
        word = input("Enter a word: ")
        words = word.split()
        
        for word in words:
            print(word*