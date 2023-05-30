#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers or adds fruits. """    
    
    # Print the numbers:
    print('Numbers: ')
    for num in range(1, 101):
        print(num)
        
    # Add fruits:
    print('Add fruits: ')
    fruits = ['apple', 'banana', 'orange']
    fruits_sum = sum(fruits)
    print('The sum of fruits: ', fruits_sum)
    
    # Print the fruits:
    print('Fruits: ')
    for fruit in fruits:
        print(fruit)
        
    # Print the sum of the fruits:
    print('The sum of the fruits: ', fruits_sum)
    
    # Print the sum of the numbers:
    print('The sum of the numbers: ', fruits_sum + 