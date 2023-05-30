#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words. """    
    words = ['hello', 'world', 'how', 'are', 'you', 'doing']
    
    # Loop forever
    while True:
        # Loop through each word
        for word in words:
            # Print the word multiplied by its index
            print(word*