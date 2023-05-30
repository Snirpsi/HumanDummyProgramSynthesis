#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['cat', 'dog', 'mouse', 'rabbit', 'monkey']
    
    # Start a loop that will iterate over the words and print them out
    for word in words:
        print(word)
        
    # Pause the program for 5 seconds
    time.sleep(5)
    
    # Stop the program when CTRL+C is pressed
    