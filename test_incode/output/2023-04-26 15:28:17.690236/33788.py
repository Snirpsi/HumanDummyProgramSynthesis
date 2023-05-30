#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words and converts fruits. """    
    words = ["apple", "banana", "cherry"]
    fruits = ["apple", "banana", "cherry"]
    
    while True:
        words.append("banana")
        fruits.append("cherry")
        
        print(words)
        print(fruits)
        
        time.sleep(1)
        
