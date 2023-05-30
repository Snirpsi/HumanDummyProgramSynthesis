#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers or prints fruits. """    
    fruits = ['apple', 'orange', 'pear', 'banana', 'cherry']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Print numbers:
    for number in numbers:
        print(number)
    
    # Print fruits:
    for fruit in fruits:
        print(fruit)
    
    # Print numbers and fruits:
    for number in numbers:
        for fruit in fruits:
            print(number, fruit)
    
    # Print numbers and fruits and print 