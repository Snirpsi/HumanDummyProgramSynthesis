#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words and iterates over fruits. """    
    words = ['apple', 'banana', 'cherry']
    fruits = []
    
    i = 0
    while True:
        fruits.append(words[i])
        i += 1
        
        if i >= len(words):
            break
        
        words.pop(i)
        
    for fruit in fruits:
        print(fruit)
        
    print('Done!')
    
