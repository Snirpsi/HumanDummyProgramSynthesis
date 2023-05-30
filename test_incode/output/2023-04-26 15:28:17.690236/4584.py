#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words and returns fruits. """    
    fruits = []
    
    for word in words:
        if word in fruits:
            fruits.remove(word)
        else:
            fruits.append(word)
    
    return fruits
