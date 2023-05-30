#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits and enumerates words. """    
    
    fruits = enumerate('apple')
    words = enumerate('banana')
    
    for fruit, word in fruits:
        print('The fruit is', fruit)
        print('The word is', word)
        
    for fruit, word in words:
        print('The fruit is', fruit)
        print('The word is', word)
        
    print('Done')
    
