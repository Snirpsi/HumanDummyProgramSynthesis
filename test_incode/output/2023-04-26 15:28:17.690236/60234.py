#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words. """    
    words = input("Enter a word: ")
    
    multiplied_words = []
    for word in words:
        multiplied_words.append(word*2)
    
    print(" ".join(multiplied_words))
    
