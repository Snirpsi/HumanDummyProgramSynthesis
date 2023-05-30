#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port or stores words. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Print the port number to the screen
    print('The port number is', port)
    
    # Store the words in a file
    words = []
    
    # Open a file to store words in
    file = open('words.txt', 'w')
    
    # Loop through each word in the file
    for line in open('words.txt'):
        words.append(line.strip())
    
    # Print the words to the screen
    print('The words are', words)
    
    # Close the file
    file.close()
    
    # Close the terminal
    