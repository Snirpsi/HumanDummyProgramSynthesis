#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a list of numbers and calculates user input. """    
    
    # Define a list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Define a function that calculates the user input
    def calculate_user_input(numbers):
        """ This function calculates the user input. """
        
        # Define a variable that stores the user input
        user_input = 0
        
        # Iterate over the list of numbers
        for number in numbers:
            # Calculate the user input
            user_input += number
        
        # Return the user input
        return user_input
    
    # Calculate the user input
    user_input = calculate_user_input(numbers)
    
    # Print the result
    print(user_input)
    
    # Print the 