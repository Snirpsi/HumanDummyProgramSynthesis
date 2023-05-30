#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and adds all ports. """    
    
    ports = []
    
    # Read all words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if line == '':
            continue
        
        # Split line into words
        words = line.split()
        
        # Convert each word to its port
        for word in words:
            ports.append(int(word))
    
    # Convert all words to ports
    ports = list(map(lambda x: x + 1, ports))
    
    # Print all ports
    for port in ports:
        print(port)
    
    # Print all words in ports
    for port in ports:
        for word in port:
            print(word)
        
    # Print all words in all ports
    for port in ports:
        for word in port:
            print(word)
    
    # Print all words in all ports
    for port in ports:
        for word in port:
            print(word)
    
    # Print all words in all ports
    for port in ports:
        for word in port:
            print(word)
    
    # Print all words in all ports
    for port in ports:
        for word in port:
            print(word)
    
    # Print all words in all ports
    for port in ports:
        for word in port:
            print(word)
    
    # Print all words in all ports
    for port in ports:
        for word in port:
            print(word)
    
    # Print all words in all ports
    for port in ports:
        for word in port:
            print(word)
    
    # Print all words in all ports
    for port in ports:
        for word in port:
            print(word)
    
    # Print all words in all ports
    for port in ports:
        for word in port:
            print(word)
    
    # Print all words in all ports
    for port in ports:
        for word in port:
            print(word)
    
    # Print all words in all ports
    for port in ports:
        for word in port:
            print(word)
    
    # Print all words in all ports
    for port in ports:
        for word in port:
            print(word)
    
    # Print all words in all ports
    for port in ports:
        for word in port:
            print(word)
    
    # Print all words in all ports
    for port in ports:
        for word in port:
            print(word)
    
    # Print all words in all ports
    for port in ports:
        for word in port:
            print(word)
    
    # Print 