#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates fruits. """    
    fruits = calc_fruits()
    
    # Print the fruit names
    for fruit in fruits:
        print(fruit)
    
    # Print the fruit counts
    for fruit in fruits:
        print(fruit + ' ' + str(fruits[fruit]))
        
    # Print the fruit totals
    for fruit in fruits:
        print(fruit + ' ' + str(fruits[fruit]) + ' 