#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a list of words and stores fruits. """    
    fruits = []
    
    for word in words:
        if word in fruits:
            fruits.remove(word)
        else:
            fruits.append(word)
    
    print(fruits)
    
