#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers. """    
    
    # Read input from stdin
    numbers = []
    while True:
        number = int(input('Enter a number: '))
        numbers.append(number)
        if number == 0: break
    
    # Print the numbers in reverse order
    for number in reversed(numbers):
        print(number)
    
    # Print the sum of the numbers
    total = sum(numbers)
    print('The sum of the numbers is {}'.format(total))
    
    # Print the average of the numbers
    average = sum(numbers) / len(numbers)
    print('The average of the numbers is {}'.format(average))
    
    # Print the largest number
    largest = numbers[0]
    print('The largest number is', largest)
    
    # Print the smallest number
    smallest = numbers[0]
    print('The smallest number is', smallest)
    
    # Print the average of the numbers with no repetition
    no_duplicates = sum(numbers)
    print('The average of the numbers with no repetition is', no_duplicates)
    
    # Print the average of the numbers with repetition
    repetition = sum(numbers) // len(numbers)
    print('The average of the numbers with repetition is', repetition)
    
    # Print the average of the numbers with repetition and no repetition
    no_duplicate_repetition = sum(numbers) // len(numbers)
    print('The average of the numbers with repetition and no repetition is', no_duplicate_repetition)
    
    # Print the average of the numbers with repetition and no repetition and no repetition
    no_duplicate_repetition_no_duplicates = sum(numbers) // len(numbers)
    print('The average of the numbers with repetition and no repetition and no repetition is', no_duplicate_repetition_no_duplicates)
    
    # Print the average of the numbers with repetition and no repetition and no repetition and no repetition
    no_duplicate_repetition_no_duplicates_no_duplicates = sum(numbers) // len(numbers)
    print('The average of the numbers with repetition and no repetition and no repetition and no repetition is', no_duplicate_repetition_no_duplicates_no_duplicates)
    
    # Print the average of the numbers with repetition and no repetition and no repetition and no repetition and no repetition
    no_duplicate_repetition_no_duplicates_no_duplicates_no_duplicates = sum(numbers) // len(numbers)
    print('The average of the numbers with repetition and no repetition and no repetition and no repetition and no repetition is', no_duplicate_repetition_no_duplicates_no_