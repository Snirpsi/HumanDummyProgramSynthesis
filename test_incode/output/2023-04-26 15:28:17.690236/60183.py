#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words or iterates over fruits. """    
    while True:
        fruits = ['apple', 'orange', 'banana', 'kiwi']
        fruits_iter = iter(fruits)
        
        for fruit in fruits_iter:
            print(