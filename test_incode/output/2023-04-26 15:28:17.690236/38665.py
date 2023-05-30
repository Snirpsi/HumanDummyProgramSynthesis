#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words and iterates over a list of numbers. """    
    words = []
    i = 0
    while i < len(words):
        words.append(str(i))
        i += 1
        
    words.sort()
    
    for word in words:
        print(word)
    
