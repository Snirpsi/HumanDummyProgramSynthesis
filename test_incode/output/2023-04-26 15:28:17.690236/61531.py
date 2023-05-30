#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes fruits. """    
    fruits = ['apple', 'banana', 'orange', 'pear', 'mango', 'plum', 'grape']
    for fruit in fruits:
        if fruit not in fruits:
            print(fruit)
            fruits.remove(fruit)
