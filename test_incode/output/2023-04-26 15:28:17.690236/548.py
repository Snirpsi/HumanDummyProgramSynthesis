#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    words = []
    
    # Open the file that contains the list of words and read it line by line.
    for line in open('words.txt'):
        line = line.strip()
        words.append(line)
    
    # Return the list of words to the client.
    return 