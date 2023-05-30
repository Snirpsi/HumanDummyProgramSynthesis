#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words and stores fruits. """    
    
    words = ['apple', 'banana', 'orange', 'pear', 'pineapple', 'grape', 'mango', 'cherry']
    fruits = []
    
    for word in words:
        fruits.append(word)
        
    fruits.sort()
    
    for fruit in fruits:
        print(fruit)
        
