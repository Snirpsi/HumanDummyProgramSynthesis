#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words or opens fruits. """    
    words = ['apple', 'banana', 'cherry']
    fruits = ['apple', 'banana', 'cherry']
    
    i = 0
    while True:
        print(words[i])
        i += 1
        if i == len(words):
            break
        
        if words[i] == 'cherry':
            fruit