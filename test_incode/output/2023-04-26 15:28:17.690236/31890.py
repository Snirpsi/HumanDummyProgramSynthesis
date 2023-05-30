#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    for fruit in fruits:
        print('{} x {} = {}'.format(fruit, fruits[0], fruits[0] * fruit))
    
    print('\nDone')
    
