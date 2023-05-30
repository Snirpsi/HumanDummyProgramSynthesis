#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words and iterates over a port. """    
    
    # Read words from file
    words = read_words()
    
    # Iterate over port
    port = read_port()
    
    # Print the words and port
    words = print_words(words)
    port = print_port(port)
    
    # Close port
    port.close()
    
    # Close file
    words.close()
    
    # Close program
    