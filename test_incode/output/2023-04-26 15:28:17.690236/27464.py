#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words. """    
    words = ['Hello', 'World']
    multiplied = [x * y for x, y in zip(words, words[1:])]
    print(multiplied)
