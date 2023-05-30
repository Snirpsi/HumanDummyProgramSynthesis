#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates user input. """    
    
    # Define a function to calculate user input
    def calc_input():
        """ Calculates user input. """
        
        # Define the user input variable
        answer = input("What is your name? ")
        
        # Return the user input variable
        return answer
    
    # Call calc_input() function to calculate user input
    answer = calc_input()
    
    # Print the answer variable
    print(answer)
    
    # Close the program with CTRL + C
