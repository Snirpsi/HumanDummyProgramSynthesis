#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over numbers and removes fruits. """    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi']
    for fruit in fruits:
        if fruit == 'apple':
            fruits.remove('apple')
        elif fruit == 'orange':
            fruits.remove('orange')
        elif fruit == 'banana':
            fruits.remove('banana')
        elif fruit == 'pear':
            fruits.remove('pear')
        elif fruit == 'kiwi':
            fruits.remove('kiwi')
    print('The fruit list after removing fruits:', fruits)
