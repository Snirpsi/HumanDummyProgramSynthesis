#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits and removes user input. """    
    fruits = list("banana")
    fruits.remove(input("Enter a fruit: "))
    print(fruits)
    
