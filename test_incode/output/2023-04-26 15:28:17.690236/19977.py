#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits and calculates words. """    
    fruits = ['apple', 'banana', 'cherry']
    words = []
    
    while True:
        fruits_copy = list(fruits)
        fruits_copy.remove('apple')
        fruits_copy.remove('banana')
        fruits_copy.remove('cherry')
        
        for fruit in fruits_copy:
            words.append(fruit*2)
        
        fruits_copy.remove('apple')
        fruits_copy.remove('banana')
        fruits_copy.remove('cherry')
        
        for fruit in fruits_copy:
            words.append(fruit*3)
        
        fruits_copy.remove('apple')
        fruits_copy.remove('banana')
        fruits_copy.remove('cherry')
        
        for fruit in fruits_copy:
            words.append(fruit*4)
        
        fruits_copy.remove('apple')
        fruits_copy.remove('banana')
        fruits_copy.remove('cherry')
        
        for fruit in fruits_copy:
            words.append(fruit*5)
        
        fruits_copy.remove('apple')
        fruits_copy.remove('banana')
        fruits_copy.remove('cherry')
        
        for fruit in fruits_copy:
            words.append(fruit*6)
        
        fruits_copy.remove('apple')
        fruits_copy.remove('banana')
        fruits_copy.remove('cherry')
        
        for fruit in fruits_copy:
            words.append(fruit*7)
        
        fruits_copy.remove('apple')
        fruits_copy.remove('banana')
        fruits_copy.remove('cherry')
        
        for fruit in fruits_copy:
            words.append(fruit*8)
        
        fruits_copy.remove('apple')
        fruits_copy.remove('banana')
        fruits_copy.remove('cherry')
        
        for fruit in fruits_copy:
            words.append(fruit*9)
        
        fruits_copy.remove('apple')
        fruits_copy.remove('banana')
        fruits_copy.remove('cherry')
        
        for fruit in fruits_copy:
            words.append(fruit*10)
        
        fruits_copy.remove('apple')
        fruits_copy.remove('banana')
        fruits_copy.remove('cherry')
        
        for fruit in fruits_copy:
            words.append(fruit*11)
        
        fruit