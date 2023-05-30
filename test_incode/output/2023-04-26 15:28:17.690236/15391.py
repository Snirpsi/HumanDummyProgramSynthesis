#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits and calculates a list of words. """    
    
    # Open the fruit list
    fruits = open('fruits.txt', 'r')
    
    # Read each line of the fruit list
    fruits_list = fruits.readlines()
    
    # Close the fruit list
    fruits.close()
    
    # Open the word list
    words = open('words.txt', 'r')
    
    # Read each line of the word list
    words_list = words.readlines()
    
    # Close the word list
    words.close()
    
    # Open the list of words to calculate 