#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens fruits. """    
    
    # Open the fruits.txt file
    fruits = open_file('fruits.txt')
    
    # Print the fruits one by one
    for line in fruits:
        print(line)
        
    # Close the fruits.txt file
    fruits.close()
    
    # Close the program
    exit(0)
