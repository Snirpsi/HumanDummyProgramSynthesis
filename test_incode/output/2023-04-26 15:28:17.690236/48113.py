#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port and adds words. """    
    port = '/dev/ttyACM0'
    
    # Open the port and read its content
    file = open(port, 'r')
    
    # Iterate over each line of the file
    for line in file:
        # Split each line into words
        words = line.split()
        
        # Iterate over each word in the line
        for word in words:
            # Print the word if it's not empty
            if word != '':
                print(word)
                
    file.close()
    
    # Close the port
    file.close()
    
