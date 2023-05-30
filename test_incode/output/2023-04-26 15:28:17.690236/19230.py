#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words and iterates over numbers. """    
    
    words = []
    
    # Iterate over numbers and add them to our word list
    for number in range(1, 10):
        words.append(str(number))
    
    # Send the list of words to the browser
    