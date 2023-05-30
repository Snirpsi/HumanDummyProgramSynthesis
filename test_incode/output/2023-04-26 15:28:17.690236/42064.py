#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits. """    
    while True:
        fruits = input("Enter the fruit names to remove: ").split()
        fruits.remove('apple')
        fruits.remove('banana')
        fruits.remove('cherry')
        fruits.remove('