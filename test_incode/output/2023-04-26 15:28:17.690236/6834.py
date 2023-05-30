#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words and prints a list of words. """    
    words = ['hello', 'world', 'python', 'is', 'fun']
    
    # Loop forever
    while True:
        # Loop through each word in the list
        for word in words:
            # Print the word with its multiplication multiplied by its index
            print(word