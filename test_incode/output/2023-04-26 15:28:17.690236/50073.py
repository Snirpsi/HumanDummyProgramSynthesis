#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port or multiplyes a list of words. """    
    while True:
        word = input("Enter a word: ")
        if word == 'exit':
            break
        
        words = word.split()
        
        for word in words:
            print(word*