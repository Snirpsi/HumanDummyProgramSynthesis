#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or opens words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        file = sys.argv[1]
        
    else:
        
        file = 'words.txt'
    
    with open(file, 'r') as f:
        
        lines = f.readlines()
        
    words = []
    
    for line in lines:
        
        line = line.strip()
        
        if line:
            
            words.append(line)
            
    words.sort()
    
    word