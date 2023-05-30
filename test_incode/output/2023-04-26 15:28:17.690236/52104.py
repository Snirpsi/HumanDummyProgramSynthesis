#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates fruits or opens a list of words. """    
    
    # Open a list with fruits or words to enumerate
    fruits = ['apple', 'banana', 'cherry']
    
    # Enumerate fruits or words
    enumerated = enumerate(fruits)
    
    # Print the fruits or words to stdout
    for fruit, value in enumerated:
        print('{} = {}'.format(fruit, value))
    
    # Print the fruits or words to stderr
    for fruit, value in enumerated:
        print('{} = {}'.format(fruit, value))
    
    # Print the fruits or words to file
    with open('fruits.txt', 'w') as file:
        for fruit, value in enumerated:
            file.write('{} = {}\n'.format(fruit, value))
    
    # Print the fruits or words to file
    with open('fruits.txt', 'r') as file:
        for fruit, value in enumerated:
            print('{} = {}'.format(fruit, value))
    
    # Print the fruits or words to file
    with open('fruits.txt', 'r') as file:
        for fruit, value in enumerated:
            print(value)
    
    # Print the fruits or words to file
    with open('fruits.txt', 'r') as file:
        for fruit in fruits:
            print(fruit)
    
    # Print the fruits or words to file
    with open('fruits.txt', 'r') as file:
        for fruit in fruits:
            print(file.readline())
    
    # Print the fruits or words to file
    with open('fruits.txt', 'r') as file:
        for fruit in fruits:
            print(file.readline())
    
    # Print the fruits or words to file
    with open('fruits.txt', 'r') as file:
        for fruit in fruits:
            print(file.readline())
    
    # Print the fruits or words to file
    with open('fruits.txt', 'r') as file:
        for fruit in fruits:
            print(file.readline())
    
    # Print the fruits or words to file
    with open('fruits.txt', 'r') as file:
        for fruit in fruits:
            print(file.readline())
    
    # Print the fruits or words to file
    with open('fruits.txt', 'r') as file:
        for fruit in fruits:
            print(file.readline())
    
    # Print the fruits or words to file
    with open('fruits.txt', 'r') as file:
        for fruit in fruits:
            print(file.readline())
    
    # Print the fruits or words to file
    with open('fruits.txt', 'r') as file:
        for fruit in fruits:
            print(file.readline())
    
    # Print the fruits or words to file
    with open('fruits.txt', 'r') as file:
        for fruit in fruits:
            print(file.readline())
    
    # 