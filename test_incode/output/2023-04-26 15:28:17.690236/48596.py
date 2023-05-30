#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates user input and iterates over a list of numbers. """    
    
    # Define a function that takes in user input
    def input_func():
        """ This function takes in user input and returns a list of numbers. """
        
        # Define a list to store the user input
        user_input = []
        
        # Iterate over the list of numbers
        for number in numbers:
            
            # Append the number to the list
            user_input.append(number)
            
        # Return the list
        return user_input
    
    # Define a function that takes in user input and returns a list of numbers, 
    # and prints out the sum of the numbers in the list
    def output_func(user_input):
        """ This function takes in user input and returns a list of numbers, 
        and prints out the sum of the numbers in the list. """
        
        # Define a list to store the user input
        sum_of_numbers = []
        
        # Iterate over the list of numbers
        for number in user_input:
            
            # Append the number to the list
            sum_of_numbers.append(number)
            
        # Print the sum of the numbers in the list
        print("The sum of all the numbers in the list is: " + str(sum(sum_of_numbers)))
        
    # Define a function that takes in user input and returns a list of numbers, 
    # and prints out the sum of the numbers in the list, and prints out the 
    # difference between the sum of the numbers in the list and the number 
    # the user input
    def difference_func(user_input):
        """ This function takes in user input and returns a list of numbers, 
        and prints out the sum of the numbers in the list, and prints out the 
        difference between the sum of the numbers in the list and the number 
        the user input. """
        
        # Define a list to store the user input
        difference_list = []
        
        # Iterate over the list of numbers
        for number in user_input:
            
            # Append the number to the list
            difference_list.append(number - user_input[0])
            
        # Print the difference between the sum of the numbers in the list and the number 
        # the user input
        print("The difference between the sum of the numbers in the list and the number "
              "the user input is: " + str(sum(difference_list)))
        
    # Define a function that takes in user input and returns a list of numbers, 
    # and prints out the sum of the numbers in the list, and prints out the 
    # difference between the sum of the numbers in the list and the number 
    # the user input, and prints out the difference between the sum of the numbers in the list 
    # and the number the user input, and prints out the difference between the sum of the numbers in the list 
    # and the number the user input, and prints out the difference between the sum of the numbers in the list 
    # and the number the user input, and prints out the difference between the sum of the numbers in the list 
    # and the number the user input, and prints 