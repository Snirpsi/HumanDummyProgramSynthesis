#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    # Open the file containing the words and read them into memory.
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    # Return the list of words.
    return words

<|/ file source=github filename=wordlist.py |>