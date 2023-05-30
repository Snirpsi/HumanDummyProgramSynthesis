#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words and stores fruits. """    
    fruits = []
    
    words = []
    
    words.append("apple")
    words.append("banana")
    words.append("cherry")
    
    fruits.append(words)
    
    for fruit in fruits:
        for word in fruit:
            print(word)
            
