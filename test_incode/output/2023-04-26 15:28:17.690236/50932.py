#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words and returns all ports. """    
    words = []
    ports = []
    
    # Read words and ports from stdin.
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
        
        words = words + get_ports(line)
        
    ports = ports + get_ports(words)
    
    # Print the ports.
    for port in ports:
        print('{}: {}'.format(port, words[port]))
        
    # Print the words.
    for word in words:
        print('{}: {}'.format(word, ports[word]))
        
    # Print the remaining words.
    for word in words:
        print('{}: {}'.format(word, ports[word]))
        
    # Print the remaining ports.
    for port in ports:
        print('{}: {}'.format(port, words[port]))
        
    # Print the remaining words.
    for word in words:
        print('{}: {}'.format(word, ports[word]))
        
    # Print the remaining ports.
    for port in ports:
        print('{}: {}'.format(port, words[port]))
        
    # Print the remaining words.
    for word in words:
        print('{}: {}'.format(word, ports[word]))
        
    # Print the remaining ports.
    for port in ports:
        print('{}: {}'.format(port, words[port]))
        
    # Print the remaining words.
    for word in words:
        print('{}: {}'.format(word, ports[word]))
        
    # Print the remaining ports.
    for port in ports:
        print('{}: {}'.format(port, words[port]))
        
    # Print the remaining words.
    for word in words:
        print('{}: {}'.format(word, ports[word]))
        
    # Print the remaining ports.
    for port in ports:
        print('{}: {}'.format(port, words[port]))
        
    # Print the remaining words.
    for word in words:
        print('{}: {}'.format(word, ports[word]))
        
    # Print the remaining ports.
    for port in ports:
        print('{}: {}'.format(port, words[port]))
        
    # Print the remaining words.
    for word in words:
        print('{}: {}'.format(word, ports[word]))
        
    # Print the remaining ports.
    for port in ports:
        print('{}: {}'.format(port, words[port]))
        
    # Print the remaining words.
    for word in words:
        print('{}: {}'.format(word, ports[word]))
        
    # Print the remaining ports.
    for port in ports:
        print('{}: {}'.format(port, words[port]))
        
    # Print the remaining words.
    for word in words:
        print('{}: {}'.format(word, ports[word]))
        
    # Print the remaining ports.
    for port in ports:
        print('{}: {}'.format(port, word