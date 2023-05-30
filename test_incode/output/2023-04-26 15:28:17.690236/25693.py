#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits and enumerates words. """    
    fruits = ['apple', 'banana', 'cherry']
    words = ['apple', 'banana', 'cherry']
    
    fruits_iter = iter(fruits)
    words_iter = iter(words)
    
    while True:
        fruit = next(fruits_iter)
        word = next(words_iter)
        
        if fruit == 'apple':
            print('The fruit %s is apple.' % word)
        elif fruit == 'banana':
            print('The fruit %s is banana.' % word)
        elif fruit == 'cherry':
            print('The fruit %s is cherry.' % word)
        else:
            print('The fruit %s is not apple or banana or cherry.' % word)
            
        fruits_iter = iter(fruits)
        words_iter = iter(words)
        
