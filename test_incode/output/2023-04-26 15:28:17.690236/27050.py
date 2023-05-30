#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words and calculates all ports. """    
    
    ports = []
    
    # Get the list of words to remove
    words = open('words.txt').read().splitlines()
    
    # Remove all words from the list
    for word in words:
        ports.append(word.strip())
    
    # Calculate all ports
    ports = list(set(ports))
    
    # Print the results
    print('\n'.join(ports))
    
    # Close the file
    words.close()
    
    # Run the server
    run(ports)
    
