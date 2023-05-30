#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers or calculates user input. """    
    
    # Open the file that contains the list of numbers
    with open('numbers.txt', 'r') as numbers:
        numbers = numbers.readlines()
    
    # Open the file that contains the user input
    with open('user_input.txt', 'r') as user_input:
        user_input = user_input.readlines()
    
    # Open the file that contains the result
    with open('result.txt', 'r') as result:
        result = result.readlines()
    
    # Print the result
    print(numbers)
    print(user_input)
    print(result)
    
    # Close the file
    numbers.close()
    user_input.close()
    result.close()
    
    # Close the program
    exit()
    
# 