#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words and iterates over all ports. """    
    words = []
    with open('words.txt', 'r') as file:
        for line in file:
            words.append(line.strip())
    
    for word in words:
        ports = find_ports(word)
        for port in ports:
            print_port(port, word)
        
