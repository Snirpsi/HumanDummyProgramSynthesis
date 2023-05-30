#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words and returns fruits. """    
    
    words = input("Enter the words: ")
    fruits = []
    
    for word in words.split():
        fruits.append(word)
    
    fruits.sort()
    
    for fruit in fruits:
        print(