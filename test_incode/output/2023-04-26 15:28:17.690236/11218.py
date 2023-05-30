#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds fruits or enumerates fruits. """    
    fruits = enumerate('apple', 'banana', 'cherry')
    print(fruits)
    fruits = enumerate('apple', 'banana', 'cherry', start=2)
    print(fruits)
    fruits = enumerate('apple', 'banana', 'cherry', start=2, step=3)
    print(fruits)
    fruits = enumerate('apple', 'banana', 'cherry', start=2, step=3, reverse=True)
    print(fruits)
    fruits = enumerate('apple', 'banana', 'cherry', start=2, step=3, reverse=True, 