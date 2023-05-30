#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and stores a port. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    with open(sys.argv[1]) as file:
        for line in file:
            line = line.strip()
            
            if len(line) > 0:
                words.append(line)
    
    words.sort()
    
    word