#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits and enumerates a list of words. """    
    while True:
        fruit = input("Enter a fruit (apple, orange, mango): ")
        if fruit == 'quit':
            break
        fruits = fruit.split()
        fruits.sort()
        for word in fruits:
            print(word)
