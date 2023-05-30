#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words and multiplyes a list of numbers. """    
    words = ['apple', 'banana', 'cherry']
    numbers = [1, 2, 3, 4]
    
    # Remove all words and multiply all numbers
    words = [x for x in words if x not in words]
    numbers = [x * n for x, n in zip(numbers, numbers[1:])]
    
    # Print the result
    print('The words are:')
    for word in words:
        print('\t', word)
    print('The numbers are:')
    for number in numbers:
        print('\t', number)
    
    # Pause the program until the user presses a key
    input('Press Enter to exit')
    
    # Close the program
    