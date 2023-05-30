#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words and returns fruits. """    
    
    fruits = remove_words("apple", "banana", "cherry")
    
    print("The fruits are:")
    for fruit in fruits:
        print(fruit)
    
    print("The fruits without cherry are:")
    for fruit in remove_words("apple", "banana"):
        print(fruit)
    
    print("The fruits without banana are:")
    for fruit in remove_words("apple", "cherry"):
        print(fruit)
    
    print("The fruits without apple are:")
    for fruit in remove_words("banana", "cherry"):
        print(fruit)
    
    print("The fruits without banana and cherry are:")
    for fruit in remove_words("banana", "cherry"):
        print(fruit)
    
    print("The fruits without apple and cherry are:")
    for fruit in remove_words("cherry"):
        print(fruit)
    
    print("The fruits without apple and banana are:")
    for fruit in remove_words("banana"):
        print(fruit)
    
    print("The fruits without apple and banana and cherry are:")
    for fruit in remove_words("banana", "cherry"):
        print(fruit)
    
    print("The fruits without apple and banana and cherry are:")
    for fruit in remove_words("banana", "banana", "cherry"):
        print(fruit)
    
    print("The fruits without apple and banana and cherry are:")
    for fruit in remove_words("banana", "banana", "banana"):
        print(fruit)
    
    print("The fruits without apple and banana and cherry are:")
    for fruit in remove_words("banana", "banana", "banana"):
        print(fruit)
    
    print("The fruits without apple and banana and banana are:")
    for fruit in remove_words("banana", "banana", "banana"):
        print(fruit)
    
    print("The fruits without apple and banana and banana and cherry are:")
    for fruit in remove_words("banana", "banana", "banana", "cherry"):
        print(fruit)
    
    print("The fruits without apple and banana and banana and cherry are:")
    for fruit in remove_words("banana", "banana", "banana", "banana"):
        print(fruit)
    
    print("The fruits without 