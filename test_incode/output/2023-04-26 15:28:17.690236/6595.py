#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    words = []
    
    # Read the words from the file 'words.txt'
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    # Return the list of words to the user
    return words

<|/ file source=github ext=.py |>