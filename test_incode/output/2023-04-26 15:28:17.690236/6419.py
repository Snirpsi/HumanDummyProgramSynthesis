#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    for fruit in fruits:
        if fruit not in ['apple', 'orange', 'banana', 'cherry']:
            print('%s is now %s ' % (fruit, fruits[fruits.index(