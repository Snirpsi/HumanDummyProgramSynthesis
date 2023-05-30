#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over numbers or calculates fruits. """    
    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    fruits = ['apple','orange','banana','cherry','pineapple','kiwi','lemon']
    
    for number in numbers:
        for fruit in fruits:
            print(number+fruit)
            
