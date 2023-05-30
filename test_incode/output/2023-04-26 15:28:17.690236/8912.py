#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words or converts a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        exit(1)
    
    port = int(sys.argv[1])
    
    words = []
    
    while True:
        line = sys.stdin.readline()
        
        if not line:
            break
        
        line = line.strip()
        
        if not line:
            continue
        
        words.append(line)
    
    print('\n'.join(words))
    
    exit(0)
    
