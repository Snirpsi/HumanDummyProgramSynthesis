#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or removes a list of words. """    
    
    port = int(sys.argv[1])
    
    if port == 0: 
        print("Please specify a port to listen on.")
        sys.exit()
    
    words = []
    
    # Read words from stdin and add to list
    for line in sys.stdin:
        line = line.strip()
        
        # Ignore empty lines
        if len(line) == 0: 
            continue
        
        # Remove any leading or trailing whitespace
        line = line.lstrip()
        line = line.rstrip()
        
        # Ignore lines that start with '#'
        if line[0] == '#': 
            continue
        
        # Ignore lines that start with '-'
        if line[0] == '-': 
            continue
        
        # Ignore lines that start with '+'
        if line[0] == '+': 
            continue
        
        # Ignore lines that start with '-'
        if line[0] == '-': 
            continue
        
        # Ignore lines that start with '+'
        if line[0] == '+': 
            continue
        
        # Ignore lines that start with '-'
        if line[0] == '-': 
            continue
        
        # Ignore lines that start with '+'
        if line[0] == '+': 
            continue
        
        # Ignore lines that start with '-'
        if line[0] == '-': 
            continue
        
        # Ignore lines that start with '+'
        if line[0] == '+': 
            continue
        
        # Ignore lines that start with '-'
        if line[0] == '-': 
            continue
        
        # Ignore lines that start with '+'
        if line[0] == '+': 
            continue
        
        # Ignore lines that start with '-'
        if line[0] == '-': 
            continue
        
        # Ignore lines that start with '+'
        if line[0] == '+': 
            continue
        
        # Ignore lines that start with '-'
        if line[0] == '-': 
            continue
        
        # Ignore lines that start with '+'
        if line[0] == '+': 
            continue
        
        # Ignore lines that start with '-'
        if line[0] == '-': 
            continue
        
        # Ignore lines that start with '+'
        if line[0] == '+': 
            continue
        
        # Ignore lines that start with '-'
        if line[0] == '-': 
            continue
        
        # Ignore lines that start with '+'
        if line[0] == '+': 
            continue
        
        # Ignore lines that start with '-'
        if line[0] == '-': 
            continue
        
        # Ignore lines that start with '+'
        if line[0] == '+': 
            continue
        
        # Ignore lines that start with '-'
        if line[0] == '-': 
            continue
        
        # Ignore lines that start with '+'
        if line[0] == '+': 
            continue
        
        # Ignore lines that start with '-'
