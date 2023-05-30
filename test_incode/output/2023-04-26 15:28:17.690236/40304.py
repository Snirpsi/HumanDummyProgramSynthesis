#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or prints user input. """    
    
    # Open the file that contains the user input
    file = open('input.txt', 'r')
    
    # Read each line of the file
    for line in file:
        
        # Print each line of the file
        print(line)
        
    # Close the file
    file.close()
    
    # Close the program
    exit(0)
    
