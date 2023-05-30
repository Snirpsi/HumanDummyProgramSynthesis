#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or returns numbers. """    
    fruits = Fruits()
    while True:
        try:
            number = fruits.next()
            print(number)
        except StopIteration:
            break
