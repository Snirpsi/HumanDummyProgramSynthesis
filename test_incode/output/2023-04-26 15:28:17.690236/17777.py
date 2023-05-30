#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words or removes fruits. """    
    
    words = input('Enter a word: ')
    
    words = words.split()
    
    fruits = input('Enter a fruit: ')
    
    fruits = fruits.split()
    
    fruits_removed = []
    
    for fruit in fruits:
        if fruit not in words:
            fruits_removed.append(fruit)
    
    for fruit in fruits_removed:
        print('The fruit ' + fru