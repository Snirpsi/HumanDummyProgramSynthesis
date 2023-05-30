#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words and stores all ports. """    
    ports = []
    
    for line in open('words.txt'):
        line = line.strip()
        ports.append(line)
    
    ports = ports[1:]
    
    for port in ports:
        print(port)
    
