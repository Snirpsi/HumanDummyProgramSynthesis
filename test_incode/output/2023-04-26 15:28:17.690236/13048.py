#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words. """    
    words = ['cat', 'dog', 'bird', 'mouse']
    
    product = 1
    for word in words:
        product *= word
    
    print(product)
    
