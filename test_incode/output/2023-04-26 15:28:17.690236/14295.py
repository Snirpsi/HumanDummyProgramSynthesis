#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words or calculates fruits. """    
    
    words = ['apple', 'banana', 'cherry', 'orange', 'pear', 'pineapple', 'plum']
    
    fruits = []
    
    for word in words:
        fruits.append(word)
        
    fruits.sort()
    
    print('Fruits:')
    for fruit in fruits:
        print(fruit)
    
    print('')
    
    print('Fruit counts:')
    
    fruits_count = {}
    
    for fruit in fruits:
        fruits_count[fruit] = fruits_count.get(fruit, 0) + 1
    
    for fruit, count in fruits_count.items():
        print(fruit, count)
    
    print('')
    
    print('Fruit counts with 