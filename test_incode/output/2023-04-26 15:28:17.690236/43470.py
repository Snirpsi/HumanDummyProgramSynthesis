#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers or opens fruits. """    
    
    # Open the fruits file
    fruits = open("fruits.txt", "r")
    
    # Read the fruits file
    fruits_data = fruits.read()
    
    # Close the fruits file
    fruits.close()
    
    # Print the fruits data
    print(fruits_data)
    
    # Close the fruits file
    fruits.close()
    
    # Close the program
    exit(0)
    
