#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words or converts a port. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    words = []
    
    with open('/etc/wordlist', 'r') as f:
        for line in f:
            line = line.strip()
            
            if line:
                words.append(line)
    
    words = words[: