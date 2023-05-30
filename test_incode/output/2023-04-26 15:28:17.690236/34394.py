#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words or converts a port. """    
    while True:
        port = int(input("Enter a port number: "))
        words = []
        
        # Store words in a list
        words.append(input("Enter a word: "))
        
        # Convert words to a port
        port = convert_port(port, words)
        
        # Print the converted port
        print("The port is", port)
        
        # Print the converted words
        print("The words were", words)
        
        # Wait for a keypress
        input()
        
