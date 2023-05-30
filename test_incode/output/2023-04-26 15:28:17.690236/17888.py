#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words and prints fruits. """    
    words = ['apple', 'orange', 'banana', 'pear']
    fruits = ['apple', 'orange', 'banana', 'pear']
    
    fruits = list(fruits)
    words = list(words)
    
    fruits.sort()
    words.sort()
    
    for fruit in fruits:
        print('%s %s' % (fruit, words[fruits.index(