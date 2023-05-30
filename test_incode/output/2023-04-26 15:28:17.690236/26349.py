#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port or stores a list of words. """    
    
    # Get the list of words from the command line arguments
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    # Add the words to the port
    port = Port()
    port.add_words(words)
    
    # Print the port
    print(port)
    
    # Print the list of words in the port
    print(port.get_words())
    
    # Print the list of words in the port in reverse
    print(port.get_words_reverse())
    
    # Print the list of words in the port in reverse
    print(port.get_words_reverse_reverse())
    
    # Print the list of words in the port in reverse
    print(port.get_words_reverse_