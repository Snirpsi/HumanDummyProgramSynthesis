#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    
    # Store fruits to file
    with open('fruits.txt', 'w') as f:
        f.write(fruits)
    
    # Read fruits from file
    with open('fruits.txt', 'r') as f:
        fruits = f.readlines()
        
    # Print the fruits
    print('Fruits:')
    for fruit in fruits:
        print(fruit)
        
    # Print the fruits without spaces
    print('\nFruits:')
    for fruit in fruits:
        print(fruit.strip())
        
    # Print the fruits without spaces
    print('\nFruits:')
    for fruit in fruits:
        print(fru