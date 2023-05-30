#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates user input or iterates over fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    # Iterate over fruits:
    for fruit in fruits:
        print(fruit)
    
    # Enumerate user input:
    fruits = input('Enter a fruit: ')
    
    # Iterate over fruits:
    for fruit in fruits:
        print(fruit)
    
    # Enumerate user input with default value:
    fruits = input('Enter a fruit: ', default='orange')
    
    # Iterate over fruits:
    for fruit in fruits:
        print(fruit)
    
    # Enumerate user input with default value and custom value:
    fruits = input('Enter a fruit: ', default='orange', value='banana')
    
    # Iterate over fruits:
    for fruit in fruits:
        print(fruit)
    
    # Enumerate user input with default value and custom value and custom key:
    fruits = input('Enter a fruit: ', default='orange', value='banana', key='fruit')
    
    # Iterate over fruits:
    for fruit in fruits:
        print(fruit)
    
    # Enumerate user input with default value and custom value and custom key and custom separator:
    fruits = input('Enter a fruit: ', default='orange', value='banana', key='fruit', separator='|')
    
    # Iterate over fruits:
    for fruit in fruits:
        print(fruit)
    
    # Enumerate user input with default value and custom value and custom key and custom separator, custom separator:
    fruits = input('Enter a fruit: ', default='orange', value='banana', key='fruit', separator='|', separator2='|')
    
    # Iterate over fruits:
    for fruit in fruits:
        print(fruit)
    
    # Enumerate user input with default value and custom value and custom key and custom separator, custom separator, custom separator:
    fruits = input('Enter a fruit: ', default='orange', value='banana', key='fruit', separator='|', separator2='|', separator3='|')
    
    # Iterate over fruits:
    for fruit in fruits:
        print(fruit)
    
    # Enumerate user input with default value and custom value and custom key and custom separator, custom separator, custom separator, custom separator:
    fruits = input('Enter a fruit: ', default='orange', value='banana', key='fruit', separator='|', separator2='|', separator3='|', separator4='|')
    
    # Iterate over fruits:
    for fruit in fruits:
        print(fruit)
    
    # Enumerate user 