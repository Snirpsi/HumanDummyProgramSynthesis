#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates fruits and enumerates words. """    
    fruits = ['apple', 'banana', 'cherry']
    words = ['apples', 'bananas', 'cherries']
    
    for fruit in fruits:
        for word in words:
            if fruit == word:
                print("%s is a %s word" % (fruit, word))
            else:
                print("%s is not a %s word" % (fruit, word))
            
