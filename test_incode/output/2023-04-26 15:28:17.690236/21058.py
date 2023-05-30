#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts fruits and iterates over user input. """    
    fruits = input("Enter fruits: ").split()
    
    for fruit in fruits:
        if fruit == 'apple':
            print('apple')
        elif fruit == 'orange':
            print('orange')
        elif fruit == 'banana':
            print('banana')
        elif fruit == 'pear':
            print('pear')
        elif fruit == 'pineapple':
            print('pineapple')
        else:
            print('not a fruit')
            
