#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input and converts words. """    
    
    # Initialize a dictionary to store user input into 
    dictionary = {}
    
    # Iterate over each character in the input
    for character in input():
        # Check if the input character is a letter
        if character.isalpha():
            # If the input character is a letter, add it to the dictionary
            dictionary[character] = True
    
    # Print the dictionary after iterating over each character
    print(dictionary)
    
    # Print the dictionary after iterating over each character and printing 
    # each key and its value
    for key, value in dictionary.items():
        print(key, value)
</cell>
<text>
Run the cell below to test your function