#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits and adds words. """    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi']
    fruits_words = []
    
    while True:
        fruits_words.append(input('Enter a fruit: '))
        
        if fruits_words[-1] == 'quit':
            break
        
        fruits_words[-1] += ' 