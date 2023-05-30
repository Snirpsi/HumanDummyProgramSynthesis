#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes fruits and calculates numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    numbers = [3, 2, 1]
    
    # Multiply each fruit by its number
    for fruit in fruits:
        numbers = numbers * fruit
    
    # Print the results
    print('The fruits and their numbers are:')
    for fruit in fruits:
        print('{}: {}'.format(fruit, numbers))
    
    # Print the sum of the numbers
    print('The sum of all numbers is {}'.format(sum(numbers)))
    
    # Print the average of the numbers
    print('The average of the numbers is {}'.format(sum(numbers) / len(numbers)))
    
    # Print the average of the numbers for each fruit
    print('The average of the numbers for each fruit is {}'.format(
        sum(numbers) / (len(numbers) * len(fruits))))
    
    # Print the average of the numbers for each fruit for each number
    print('The average of the numbers for each fruit for each number is {}'.format(
        sum(numbers) / (len(numbers) * len(fruits)) * len(fruits))
    )
    
    # Print the average of the numbers for each fruit for each number for each fruit
    print('The average of the numbers for each fruit for each number for each fruit is {}'.format(
        sum(numbers) / (len(numbers) * len(fruits)) * len(fruits)) * len(fruits)
    ))
    
    # Print the average of the numbers for each fruit for each number for each fruit for each number
    print('The average of the numbers for each fruit for each number for each fruit for each number is {}'.format(
        sum(numbers) / (len(numbers) * len(fruits)) * len(fruits)) * len(fruits)) * len(fruits)
    ))
    
    # Print the average of the numbers for each fruit for each number for each fruit for each number for each fruit
    print('The average of the numbers for each fruit for each number for each fruit for each number for each fruit is {}'.format(
        sum(numbers) / (len(numbers) * len(fruits)) * len(fruits)) * len(fruits)) * len(fruits)
    ))
    
    # Print the average of the numbers for each fruit for each number for each fruit for each number for each fruit for each number
    print('The average of the numbers for each fruit for each number for each fruit for each number for each fruit for each number is {}'.format(
        sum(numbers) / (len(numbers) * len(fruits)) * len(fruits)) * len(fruits)) * len(fruits)
    ))
    
    # Print the average of the numbers for each fruit for each number for each fruit for each number for each fruit for each number for each fruit
    print('The average of the numbers for each fruit for each number for each fruit for each number for each fruit for each number for each fruit is {}'.format(
        sum(numbers) / (len(numbers) * len(fruit