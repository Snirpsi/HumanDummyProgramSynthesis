#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores fruits. """    
    
    fruit = Fruit("apple", "orange", "banana")
    
    fruit.add("pear")
    fruit.add("orange")
    fruit.add("banana")
    
    print(fruit)
    
    fruit.