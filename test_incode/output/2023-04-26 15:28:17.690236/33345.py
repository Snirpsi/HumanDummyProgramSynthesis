#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words and opens fruits. """    
    
    words = ["apple", "banana", "cherry"]
    
    fruits = []
    
    for word in words:
        fruits.append(open_fruit(word))
    
    print(fruits)
    
