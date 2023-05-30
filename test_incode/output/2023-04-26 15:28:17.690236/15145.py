#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input. """    
    
    # Define a function to iterate over user input
    def iterate():
        """ Iterates over user input. """
        
        # Define a variable for the user input
        choice = input("Enter your choice: ")
        
        # Print the choice
        print("Your choice is: {}".format(choice))
        
        # Return the choice
        return choice
    
    # Iterate over user input
    choice = iterate()
    
    # Print the choice
    print("Your choice is: {}".format(choice))
    
    # Return the choice
    return choice
