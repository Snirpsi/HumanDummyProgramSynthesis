#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words. """    
    while True:
        words = input("Enter a word: ")
        words = [word.lower() for word in words.split()]
        
        for word in words:
            print(word*2)
            
