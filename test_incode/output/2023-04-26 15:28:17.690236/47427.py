#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words and calculates user input. """    
    
    # Initialize a list to hold user input
    words = []
    
    # Iterate over the words in the list
    for word in words:
        # Ask the user for input
        answer = input("Enter your word: ")
        
        # Append the answer to our list
        words.append(answer)
        
        # Print the list to the screen
        print("Your word is", answer)
        
    # Print the final list
    print("Your word is", words[-1])
    
    # Close the program and quit 