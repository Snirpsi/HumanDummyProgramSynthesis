#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words or calculates numbers. """    
    
    # Open the file containing the list of words or numbers
    file = open('words.txt', 'r')
    
    # Read the file line by line
    for line in file:
        
        # Split the line into words
        words = line.split(' ')
        
        # Print the word
        print(words)
        
        # Calculate the sum of the numbers
        sum = 0
        for word in words:
            sum += int(word)
        
        # Print the sum
        print(sum)
        
    # Close the file
    file.close()
    
