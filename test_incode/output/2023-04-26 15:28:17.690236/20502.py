#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input. """    
    
    # Open the file that contains the user input
    file = open('input.txt', 'r')
    
    # Read the first line of the file
    line = file.readline()
    
    # Print the first line of the file
    print(line)
    
    # Print the second line of the file
    print(file.readline())
    
    # Close the file
    file.close()
    
    # Close the program
    exit()
    
# End of file

<|/ file source=github |>