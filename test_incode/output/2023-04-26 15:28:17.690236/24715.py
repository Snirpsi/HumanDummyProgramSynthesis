#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words or adds a list of numbers. """    
    
    # Open the file with the list of numbers
    with open('numbers.txt', 'r') as numbers:
        numbers = numbers.readlines()
        
    # Iterate over the numbers and add them to the list
    for number in numbers:
        numbers.append(int(number))
        
    # Print the list to the screen
    print(numbers)
    
    # Close the file
    numbers.close()
    
    # Close the program
    exit(0)
    
