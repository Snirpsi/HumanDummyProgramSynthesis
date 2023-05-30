#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes fruits or multiplyes words. """    
    fruit = input("Enter a fruit: ")
    word = input("Enter a word: ")
    fruit = fruit.lower()
    word = word.lower()
    
    if fruit == "apple" or fruit == "apples":
        fruit = fruit.replace("apple", "apples")
    elif fruit == "banana" or fruit == "bananas":
        fruit = fruit.replace("banana", "bananas")
    elif fruit == "cherry" or fruit == "cherries":
        fruit = fruit.replace("cherry", "cherries")
    elif fruit == "lemon" or fruit == "lemons":
        fruit = fruit.replace("lemon", "lemons")
    elif fruit == "orange" or fruit == "oranges":
        fruit = fruit.replace("orange", "oranges")
    elif fruit == "peach" or fruit == "peaches":
        fruit = fruit.replace("peach", "peaches")
    elif fruit == "plum" or fruit == "plums":
        fruit = fruit.replace("plum", "plums")
    elif fruit == "raspberry" or fruit == "raspberr