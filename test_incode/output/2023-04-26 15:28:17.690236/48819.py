#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits or adds a list of numbers. """    
    while True:
        fruit = input("Enter a fruit (apple, orange, mango, grape, peach, kiwi, lemon, watermelon, mango): ")
        if fruit == "quit":
            break
        elif fruit == "add":
            fruits = input("Enter a list of numbers: ")
            fruits = fruits.split()
            fruits = list(fruits)
            fruits.append(fruit)
            print(*fruits, sep=", ")
        else:
            print(*fruit, sep=", ")
