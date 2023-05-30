#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words and multiplyes all ports. """    
    
    # Read in words and ports
    words = input("Enter words: ")
    ports = input("Enter ports: ")
    
    # Convert words and ports to integers
    words = words.split()
    ports = ports.split()
    
    # Add words and ports
    words += ports
    
    # Convert back to string
    words = " ".join(words)
    
    # Print the result
    print(words)
    
