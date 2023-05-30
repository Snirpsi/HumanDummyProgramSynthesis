#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a list of words or enumerates all ports. """    
    
    # Read in words and ports
    words = []
    ports = []
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if len(line) == 0:
            continue
        
        # Split into words
        words = line.split()
        
        # Skip empty words
        if len(words) == 0:
            continue
        
        # Split into ports
        ports = line.split()
        
        # Skip empty ports
        if len(ports) == 0:
            continue
        
        # Append words and ports
        words.append(words[0])
        ports.append(ports[0])
    
    # Print all words and ports
    print(" ".join(words))
    print(" ".join(ports))
    
    # Iterate over ports
    for port in ports:
        print(port)
        
    # Iterate over words
    for word in words:
        print(word)
        
    # Iterate over all ports
    for port in ports:
        print(port)
        
    # Iterate over all words
    for word in words:
        print(word)
        
    # Iterate over all words and ports
    for word in words:
        for port in ports:
            print(word)
            print(port)
        
