#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input. """    
    
    # Open user input
    filename = input('Enter a filename: ')
    
    # Open the file
    file = open(filename, 'r')
    
    # Print the contents of the file
    content = file.read()
    print(content)
    
    # Close the file
    file.close()
    
    # Close the program
    exit()
    
