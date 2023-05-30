#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words and opens all ports. """    
    
    # Open all ports
    ports = openports()
    
    # Enumerate all words in ports
    words = []
    for port in ports:
        words.extend(port.scan())
        
    # Print all words in ports
    for word in words:
        print(word)
        
