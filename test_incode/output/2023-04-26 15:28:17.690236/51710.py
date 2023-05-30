#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words or removes all ports. """    
    ports = remove_ports()
    
    # Print the list of ports
    print("\nPorts:")
    for port in ports:
        print(port)
    
    # Print the list of words without ports
    print("\nWords without ports:")
    for word in words:
        print(word)
    
    # Print the list of words with ports
    print("\nWords with ports:")
    for word in words:
        if port in word:
            print(word)
    
    # Print the list of words with ports and spaces
    print("\nWords with ports and spaces:")
    for word in words:
        if port in word:
            print(word + " ")
    
    # Print the list of words with ports and spaces and new lines
    print("\nWords with ports and spaces and new lines:")
    for word in words:
        if port in word:
            print(word + "\n")
    
    # Print the list of words with ports and spaces and new lines and spaces
    print("\nWords with ports and spaces and new lines and spaces:")
    for word in words:
        if port in word:
            print(word + " " + " 