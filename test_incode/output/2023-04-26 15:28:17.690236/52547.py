#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes fruits or converts a list of numbers. """    
    
    fruit = input("Enter a fruit: ")
    fruitList = input("Enter a list of numbers: ")
    
    fruitList = [int(x) for x in fruitList.split(",")]
    
    fruitList = [x*fruit for x in fruitList]
    
    print(fruitList)
    
