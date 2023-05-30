#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores numbers or prints a list of words. """    
    
    # Read input from STDIN
    line = sys.stdin.readline()
    
    # Print the line
    print(line)
    
    # Print the list of words
    words = line.split()
    for word in words:
        print(word)
    
    # Close the file
    file.close()
    
