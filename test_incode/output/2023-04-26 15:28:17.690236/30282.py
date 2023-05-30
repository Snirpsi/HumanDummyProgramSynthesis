#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words and multiplyes a list of words. """    
    words = ['apple', 'banana', 'cherry']
    multipliedWords = []
    
    for word in words:
        multipliedWords.append(word*2)
    
    print(multipliedWords)
    
