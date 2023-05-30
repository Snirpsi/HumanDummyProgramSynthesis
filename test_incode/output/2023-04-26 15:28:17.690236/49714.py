#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words and returns words. """    
    while True:
        words = []
        words = input("Enter a word: ")
        words = words.split()
        
        if len(words) == 0:
            break
        
        words = [x * y for x, y in zip(words, words)]
        
        print(", ".join(words))
        
    
