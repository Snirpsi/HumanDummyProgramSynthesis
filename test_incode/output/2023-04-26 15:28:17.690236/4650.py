#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints fruits and prints words. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    words = ['apple', 'orange', 'banana', 'cherry']
    
    for fruit in fruits:
        for word in words:
            if fruit == word:
                print('{} is a fruit'.format(fruit))
            else:
                print('{} is not a fruit'.format(fruit))
                
