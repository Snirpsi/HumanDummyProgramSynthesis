#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input or opens fruits. """    
    
    # Open a fruit list
    fruits = open_fruits()
    
    # Enumerate user input
    enumerate_user_input(fruits)
    
    # Close the fruit list
    close_fruits(fruits)
    
