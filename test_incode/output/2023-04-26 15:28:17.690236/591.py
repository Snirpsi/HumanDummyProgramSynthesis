#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input and returns a list of numbers. """    
    
    # Initialize list
    numbers = []
    
    # Read user input
    while True:
        # Read user input
        number = int(input('Enter a number: '))
        
        # Append number to list
        numbers.append(number)
        
        # Exit loop if user enters -1
        if number == -1:
            break
    
    # Print list
    print('The numbers entered are:')
    for number in numbers:
        print(number)
        
    # Print number of numbers
    print('There are {} numbers in the list.'.format(len(numbers)))
    
    # Print average of numbers
    print('The average of the numbers entered are:')
    average = sum(numbers) / len(numbers)
    print('The average of the numbers entered are: {}'.format(average))
    
    # Print sum of numbers
    print('The sum of all the numbers entered are:')
    total = sum(numbers)
    print('The sum of all the numbers entered are: {}'.format(total))
    
    # Print sum of squares of numbers
    print('The sum of squares of the numbers entered are:')
    total2 = sum(numbers * numbers)
    print('The sum of squares of the numbers entered are: {}'.format(total2))
    
    # Print difference of numbers
    print('The difference of the numbers entered are:')
    difference = numbers[0] - numbers[1]
    print('The difference of the numbers entered are: {}'.format(difference))
    
    # Print difference of squares of numbers
    print('The difference of the squares of the numbers entered are:')
    difference2 = numbers[0] ** 2 - numbers[1] ** 2
    print('The difference of the squares of the numbers entered are: {}'.format(difference2))
    
    # Print difference of numbers and squares of numbers
    print('The difference of the numbers and squares of the numbers entered are:')
    difference3 = numbers[0] - numbers[1] ** 2
    print('The difference of the numbers and squares of the numbers entered are: {}'.format(difference3))
    
    # Print difference of numbers and squares of numbers with exponent
    print('The difference of the numbers and squares of the numbers entered are:')
    difference4 = numbers[0] ** 2 - numbers[1] ** 3
    print('The difference of the numbers and squares of the numbers entered are: {}'.format(difference4))
    
    # Print difference of numbers and squares of numbers with exponent
    print('The difference of the numbers and squares of the numbers entered are:')
    difference5 = numbers[0] ** 2 - numbers[1] ** 4
    print('The difference of the numbers and squares of the numbers entered are: {}'.format(difference5))
    
    # Print difference of numbers and squares of numbers with exponent
    print('The difference of the numbers and squares of the numbers entered are:')
    difference6 = numbers[0] ** 2 - numbers[1] ** 5
    print('The difference of the numbers and squares of the numbers entered are: {}'.format(difference6))
