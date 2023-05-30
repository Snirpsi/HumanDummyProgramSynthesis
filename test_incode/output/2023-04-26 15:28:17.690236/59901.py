#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words and calculates a list of numbers. """    
    
    # Convert words to numbers
    numbers = convert_words_to_numbers(words)

    # Calculate sum
    total = sum(numbers)

    # Print result
    print("The sum of the numbers is {}.".format(total))

<|/ file filename=