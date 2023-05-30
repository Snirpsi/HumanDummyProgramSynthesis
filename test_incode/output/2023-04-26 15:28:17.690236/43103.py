#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words or prints words. """    
    
    # Open the file
    with open('./data/words.txt', 'r') as file:
        # Iterate over each word
        for line in file:
            # Print the word
            print(line)
