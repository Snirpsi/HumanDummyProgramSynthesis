#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words and returns fruits. """    
    fruits = []
    while True:
        fruits.append(input("Enter a fruit: "))
        if fruits[-1] == 'quit':
            break
    print("The fruits are {}".format(