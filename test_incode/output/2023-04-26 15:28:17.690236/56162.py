#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words. """    
    words = ['cat', 'dog', 'bird', 'snake']
    
    multiplied = []
    for word in words:
        multiplied.append(word*2)
    
    print(multiplied)
    
