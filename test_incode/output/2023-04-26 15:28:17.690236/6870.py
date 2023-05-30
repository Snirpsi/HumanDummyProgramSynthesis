#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts fruits or removes a list of words. """    
    
    fruit = input("Enter a fruit or remove a word from the list: ")
    
    if fruit == 'fruit':
        fruit = 'apple'
    elif fruit == 'remove':
        fruit = 'apple'
    else:
        print("Invalid input")
        
    fruits = input("Enter the list of fruits: ")
    
    fru