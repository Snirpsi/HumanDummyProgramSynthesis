#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts user input or converts a list of numbers. """    
    
    # Get the input from the user
    number = int(input('Enter a number: '))
    
    # Convert the input to a list
    numbers = list(map(int, input('Enter a number: ')))
    
    # Print the list
    print('The numbers are: ', numbers)
    
    # Print the sum of the numbers
    print('The sum of all the numbers is ', sum(numbers))
    
    # Print the average of the numbers
    print('The average of the numbers is ', sum(numbers) / len(numbers))
    
    # Print the standard deviation of the numbers
    print('The standard deviation of the numbers is ', math.sqrt((sum(numbers)-sum(numbers)*len(numbers))/len(numbers)))
    
    # Print the variance of the numbers
    print('The variance of the numbers is ', math.pow(sum(numbers)-sum(numbers)*len(numbers),2))
    
    # Print the median of the numbers
    print('The median of the numbers is ', sorted(numbers)[int(len(numbers)/2)]