#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts fruits. """    
    fruits = ['apple', 'orange', 'banana', 'grape', 'kiwi', 'pear']
    fruits.sort()
    fruits.reverse()
    fruits.insert(0, fruits.pop())
    print(fruits)

<|/ file ext=.py source=github |>