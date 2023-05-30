#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or adds user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'words.txt'
    
    with open(filename) as file:
        lines = file.readlines()
        
    words = []
    for line in lines:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
        
    words.sort()
    
    