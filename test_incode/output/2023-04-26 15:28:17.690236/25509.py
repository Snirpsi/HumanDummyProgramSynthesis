#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words or converts a port. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python add_words_to_port.py <port>")
        exit(1)
    
    port = sys.argv[1]
    
    words = sys.argv[2:]
    
    for word in words:
        add_word(port)
        
    print("Done.")
    
