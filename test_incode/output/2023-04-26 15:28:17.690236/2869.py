#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words and removes fruits. """    
    
    words = ['apple', 'banana', 'orange', 'pear', 'grape', 'mango', 'grapefruit', 'apples', 'bananas', 'oranges', 'pears', 'grapes', 'mangoes', 'grapefruits', 'apples', 'bananas', 'oranges', 'pears', 'grapes', 'mangoes', 'grapefruits']
    
    fruits = ['apples', 'bananas', 'oranges', 'pears', 'grapes', 'mangoes', 'grapefruits']
    
    words_to_remove = set(words)
    fruits_to_remove = set(fruits)
    
    words_to_remove.difference_update(fruits_to_remove)
    
    print('\n'.join([word for word in words_to_remove if word not in words_to_remove]))
    print('\n'.join([fruit for fruit in fruits_to_remove if fruit not in fruits_to_remove]))
    
