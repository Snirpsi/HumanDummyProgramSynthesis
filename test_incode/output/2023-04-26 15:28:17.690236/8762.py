#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input. """    
    
    # Open user input file
    file = open("input.txt", "r")
    
    # Read user input file
    line = file.readline()
    
    # Print user input file
    print(line)
    
    # Close user input file
    file.close()
    
    # Close program
    exit(0)
    
# End of program
