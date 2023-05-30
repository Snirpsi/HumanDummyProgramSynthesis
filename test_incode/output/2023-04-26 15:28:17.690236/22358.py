#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits. """    
    fruits = enumerate('apple', 'banana', 'cherry')
    for fruit, count in fruits:
        print('%s has %d apples and %d bananas' % (fruit, count, count*2))

<|/ file filename=