#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words and calculates fruits. """    
    words = ["apple", "banana", "cherry"]
    fruits = ["apple", "banana", "cherry"]
    
    fruits_sum = 0
    
    for word in words:
        for fruit in fruits:
            fruits_sum += fruit
            
    print(fruits_sum)
    
