#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words. """    
    words = []
    
    # Read a line from the file
    line = sys.stdin.readline()
    
    # Append the line to the list of words
    words.append(line)
    
    # Print the list of words
    print(words)
    
    # Close the file
    sys.stdin.close()
    
    # Return the list of words
    return words
