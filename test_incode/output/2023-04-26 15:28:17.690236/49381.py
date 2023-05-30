#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words or iterates over fruits. """    
    fruit = input("Enter a fruit: ")
    fruit = fruit.lower()
    fruits = [fruit]
    
    while fruit not in fruits:
        fruit = input("Enter a fruit: ")
        fruit = fruit.lower()
        fruits.append(fruit)
    
    return fruits

<|/ file ext=.py source=github |>