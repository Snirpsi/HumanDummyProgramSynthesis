#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words and opens fruits. """    
    
    words_to_remove = ["apple", "banana", "cherry"]
    
    fruits = ["apple", "banana", "cherry"]
    
    fruits_cleaned = []
    
    while len(words_to_remove) > 0:
        
        fruits_cleaned.append(fruits.pop(0))
        
        words_to_remove.remove(fruits_cleaned.pop(0))
        
    print(