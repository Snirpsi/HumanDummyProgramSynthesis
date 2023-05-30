#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits and opens numbers. """    
    
    # Open the file with the list of fruits
    with open('fruit.txt', 'r') as f:
        # Iterate over the lines of the file
        for line in f:
            # Split the line into words
            words = line.split()
            # Print the words and count how many times they occur
            print(' '.join(words), 