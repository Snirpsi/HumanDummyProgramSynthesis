#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words. """    
    
    # Load a text file
    file = open('words.txt', 'r')
    
    # Read all lines in the file
    lines = file.readlines()
    
    # Print the lines in the file
    for line in lines:
        print(line)
    
    # Close the file
    file.close()
    
    # Print the result
    print('The words are:')
    for line in lines:
        print(line)
    
    # Close the file
    file.close()
    
