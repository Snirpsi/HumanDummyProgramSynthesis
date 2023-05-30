#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words and multiplyes fruits. """    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi', 'grapes', 'watermelon']
    words = ['apple', 'orange', 'banana', 'pear', 'kiwi', 'grapes', 'watermelon']
    
    for fruit in fruits:
        for word in words:
            print('{} x {} = {}'.format(fruit, word, fruit*word))
        
