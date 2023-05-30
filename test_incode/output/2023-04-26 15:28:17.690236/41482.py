#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores fruits. """    
    
    # Create a fruit object
    apple = Fruit('apple')
    
    # Create a fruit object
    orange = Fruit('orange')
    
    # Create a fruit object
    grape = Fruit('grape')
    
    # Create a fruit object
    peach = Fruit('peach')
    
    # Create a fruit object
    grapefruits = [apple, orange, grape, peach]
    
    # Print the fruit object
    for fruit in grapefruits:
        print(fruit)
    
    # Print the fruit object
    for fruit in grapefruits:
        print(fruit.name)
    
    # Print the fruit object
    for fruit in grapefruits:
        print(fruit.