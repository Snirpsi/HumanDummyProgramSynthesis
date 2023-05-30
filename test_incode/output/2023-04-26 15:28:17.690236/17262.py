#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words and enumerates a port. """    
    
    # Create a port
    port = Port() # Create port
    
    # Add words to port
    port.add_word('word')
    port.add_word('word')
    port.add_word('word')
    
    # Enumerate port
    port.enumerate_words()
    
    # Print port contents
    print(port)
    
    # Close port
    port.close()
    
    # Close program
    sys.exit()
    
