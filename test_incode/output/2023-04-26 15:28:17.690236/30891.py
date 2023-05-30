#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words and iterates over user input. """    
    
    # Define the list of words to be multiplied
    words = ['cat', 'dog', 'mouse', 'elephant', 'lion', 'cow', 'horse']
    
    # Define the word multiplier to be used
    multiplier = 1
    
    # Iterate over the words and multiply each one
    for word in words:
        multiplier = multiplier * word
    
    # Print the result
    print(multiplier)
    
    # 