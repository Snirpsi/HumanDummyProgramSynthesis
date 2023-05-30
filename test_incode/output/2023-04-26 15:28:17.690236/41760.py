#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words and adds a port. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    with open('words.txt') as file:
        for line in file:
            line = line.strip()
            words.append(line)
    
    words.sort()
    
    word