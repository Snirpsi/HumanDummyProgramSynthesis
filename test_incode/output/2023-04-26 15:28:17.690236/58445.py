#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words or opens a port. """    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 9000
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
        
    words.reverse()
    
    words = [word.upper() for word in words]
    
    for line in words:
        print(line, end='')
        
