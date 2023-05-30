#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores fruits or adds a list of words. """    
    
    # read fruits from file
    fruits = read_fruits()
    
    # add words to fruits
    fruits = add_words(fruits)
    
    # print fruits 