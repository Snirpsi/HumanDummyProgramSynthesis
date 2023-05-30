#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words or prints numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        sys.stdout.write(sys.argv[1])
    else:
        sys.stdout.write('Words: ')
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        if line[0] == '#':
            continue
        
        words.append(line)
        
    sys.stdout.write('\n'.join(words))
    
