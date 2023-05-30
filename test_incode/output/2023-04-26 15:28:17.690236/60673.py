#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and prints words. """    
    port = int(input("Enter a port number: "))
    words = []
    
    # Loop forever
    while True:
        words.append(input("Enter a word: "))
        
        # Print the word
        print("The word is: " + " ".join(words))
        
        # Increment the port
        port += 1
        
        # Exit the loop if port is 