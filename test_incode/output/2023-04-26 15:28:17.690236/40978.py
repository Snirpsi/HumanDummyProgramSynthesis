#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words and removes numbers. """    
    words = []
    
    for word in open('words.txt'):
        words.append(word.rstrip())
        
    for word in words:
        if word.isdigit():
            words.remove(word)
    
    for word in words:
        print(word)
    
