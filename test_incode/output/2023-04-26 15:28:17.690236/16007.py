#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        for fruit in fruits:
            print('{} x {} = {}'.format(fruit, len(fruits), fruit*len(fruits)))
        time.sleep(1)
