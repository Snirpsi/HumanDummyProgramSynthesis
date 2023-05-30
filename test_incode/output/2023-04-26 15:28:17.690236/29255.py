#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words or converts fruits. """    
    
    fruit = input("Enter a fruit: ")
    
    fruitList = fruit.split()
    
    fruitDict = {}
    
    for fruit in fruitList:
        fruitDict[fruit] = 