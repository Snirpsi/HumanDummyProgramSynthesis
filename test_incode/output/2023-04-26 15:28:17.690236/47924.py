#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes fruits. """    
    fruits = ['apple', 'orange', 'banana', 'kiwi']
    
    for fruit in fruits:
        fruit = fruit.upper()
        
        if fruit == 'APPLE':
            print('apple')
        elif fruit == 'ORANGE':
            print('orange')
        elif fruit == 'BANANA':
            print('banana')
        elif fruit == 'KIWI':
            print('kiwi')
        else:
            print('unknown fruit')
            
