#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words or enumerates fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    
    # Iterate over all fruits and print their multiplication
    for fruit in fruits:
        print(fruit * 2)
    
    # Print all fruits as a list
    print(fruits)
    
    # Print all fruits as a string
    print(fruits.__str__())
    
    # Print all fruits as a tuple
    print(fruits.__tuple__())
    
    # Print all fruits as a dictionary
    print(fruits.__dictobj__())
    
    # Print all fruits as a set
    print(fruits.__set