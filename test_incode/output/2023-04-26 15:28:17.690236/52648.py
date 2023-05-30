#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words and removes all ports. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <file> <port>' % sys.argv[0])
        sys.exit()
    
    file = sys.argv[1]
    port = sys.argv[2]
    
    with open(file) as f:
        lines = f.readlines()
    
    words = []
    for line in lines:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        words = words + line.split()
    
    words = [word for word in words if word[0] != '#']
    
    with open(file, 'w') as f:
        for line in words:
            f.write('%s\n' % line)
    
    print('%s is now %s.' % (file, port))
    
