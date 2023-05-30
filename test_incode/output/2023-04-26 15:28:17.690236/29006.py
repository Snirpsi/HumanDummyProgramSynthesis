#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words or removes a port. """    
    
    port = "8080"
    
    while True:
        words = []
        
        # Read a line from the user
        line = input()
        
        # Split it into words
        words = line.split(" ")
        
        # Remove any port
        words = [word for word in words if word != port]
        
        # Print the results
        print("\n".join(words))
        
        # Wait for a keypress
        input()
        
        # Print the result