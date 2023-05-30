#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words and converts user input. """    
    
    # Get the input from the user
    words = input("Enter a word: ")
    
    # Convert the input to a list
    words = words.split()
    
    # Multiply the list with the user input
    product = words[0] * words[1]
    
    # Display the result
    print(product)
    
    # Close the program
