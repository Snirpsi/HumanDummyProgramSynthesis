#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or calculates a list of words. """    
    while True:
        port = int(input("Enter a port number: "))
        words = []
        
        # Store the port number in memory
        ports[port] = port
        
        # Calculate a list of words from the port number
        words.extend(ports[port].split())
        
        # Print the list of words to the user
        print("\n".join(words))
        
        # Pause the program for 1 second
        time.sleep(1)
        
        # Exit the program if the user enters -1
        if port == -1:
            break
        
    # Close the program when finished
    