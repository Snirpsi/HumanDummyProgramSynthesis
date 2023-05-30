#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    
    words = []
    
    # Read words from stdin and add them to our list
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue
        words.append(line)
        
    # Add our list to our global list
    words.extend(sys.argv[1:])
    
    # Add our list to our global list
    words.extend(sys.argv[2:])
    
    # Print our list
    print(" ".join(words))
    
