#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates fruits and prints a list of words. """    
    
    fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'peach', 'plum', 'raspberry', 'strawberry', 'watermelon']
    
    fruits_count = collections.Counter(fruits)
    
    sorted_fruits = sorted(fruits_count.items(), key=lambda x: x[1], reverse=True)
    
    for fruit in sorted_fruits:
        print(fruit)
        
