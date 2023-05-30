#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits. """    
    fruits = ['apple', 'banana', 'orange', 'kiwi', 'grapes', 'mango']
    while True:
        for fruit in fruits:
            print(fruit)
            time.sleep(1)
