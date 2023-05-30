#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input. """    
    
    # Open user input file
    file = open('user_input.txt', 'r')
    
    # Read user input file
    user_input = file.read()
    
    # Close user input file
    file.close()
    
    # Print user input
    print(user_input)
    
    # Close program
    exit()
    
# End of program
