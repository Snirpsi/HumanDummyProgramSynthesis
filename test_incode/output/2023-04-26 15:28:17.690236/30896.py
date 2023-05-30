#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words or calculates all ports. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
    
    ports = []
    
    for line in words:
        
        line = line.split()
        
        if len(line) == 1:
            continue
        
        ports.append(int(line[0]))
    
    ports.sort()
    
    for port in ports:
        
        print('http://127.0.0.1:%d/' % port)
        
