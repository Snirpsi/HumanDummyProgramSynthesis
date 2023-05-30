#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits and converts fruits. """    
    fruits = enumerate('apple', 'banana', 'cherry')
    for fruit, count in fruits:
        print('{} has {} apples and {} bananas.'.format(fruit, count, count*2))
    print('Done!')
    
