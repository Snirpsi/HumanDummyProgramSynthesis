#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of numbers or opens fruits. """    
    fruits = enumerate('apple', 'banana', 'cherry') 
    for fruit, count in fruits:
        print('%5s: %s' % (fruit, count))
        
    print('\nA fruit that has appeared %d times:' % fruits.count(