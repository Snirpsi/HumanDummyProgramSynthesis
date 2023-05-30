#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    words = []
    for line in lines:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
    
    words.sort()
    
    for word in words:
        print(word)
    
