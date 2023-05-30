#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words or adds fruits. """    
    
    # Read the file containing all the fruits you want to remove
    fruits = open('fruits.txt', 'r')
    
    # Read each line of the file
    for line in fruits:
        
        # Split the line into words
        words = line.split(' ')
        
        # Remove each word from the list
        fruits.remove(words)
        
    # Print the list again
    print(fruits)
    
    # Close the file
    fruits.close()
    
    # Close the program
    exit(0)
    
# End of program
