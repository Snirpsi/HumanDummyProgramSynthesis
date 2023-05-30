#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input and opens a list of numbers. """    
    
    # Open a text file containing the list of numbers and read it into a list
    numbers = open('numbers.txt', 'r')
    numbers_list = numbers.readlines()
    
    # Iterate over the list and print the numbers to the screen
    for number in numbers_list:
        print(number)
        
    # Close the file
    numbers.close()
    
    # 