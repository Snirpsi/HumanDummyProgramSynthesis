#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input and multiplyes user input. """    
    
    # Open the file that contains the user input
    file = open('input.txt', 'r')
    
    # Read user input from the file
    user_input = file.read()
    
    # Multiply user input by 2
    multiplied_input = user_input * 2
    
    # Print the multiplied input
    print(multiplied_input)
    
    # Close the file
    file.close()
    
    # Close the program
    exit(0)
    
# End of program
