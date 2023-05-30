#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words and removes a port. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line or line[0] == '#':
            continue
        
        words.append(line)
    
    words.sort()
    
    for word in words:
        
        if word in sys.argv[1:]:
            
            sys.stdout.write(word)
            
        else:
            
            sys.stdout.write(' ')
            
    sys.stdout.write('\n')
    
