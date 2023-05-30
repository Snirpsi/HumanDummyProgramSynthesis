#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words or converts numbers. """    
    
    # Open the file
    file = open('words.txt', 'r')
    
    # Read all the words and put them in a list
    words = file.read().split()
    
    # Close the file
    file.close()
    
    # Print the list
    print(words)
    
    # Convert each word to an integer
    words = [int(word) for word in words]
    
    # Print the converted list
    print(words)
    
    # Close the file
    file.close()
    
    # Close the program
    exit()
    
# End of program
