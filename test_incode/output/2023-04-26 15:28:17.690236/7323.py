#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or opens fruits. """    
    
    # Open the fruits.txt file
    with open('fruits.txt', 'r') as file:
        fruits = file.read().splitlines()
    
    # Print the fruits one by one
    for fruit in fruits:
        print(fruit)
    
    # Close the fruits.txt file
    file.close()
    
    # Close the program
    exit(0)
    
# End of program
