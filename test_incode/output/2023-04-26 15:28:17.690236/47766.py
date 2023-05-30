#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    # Read the words from a file
    for line in sys.stdin:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        words.append(line)
    
    # Print the list of words
    for word in words:
        print(word)
        
    # Start the webserver
    webserver.serve_forever()
    
