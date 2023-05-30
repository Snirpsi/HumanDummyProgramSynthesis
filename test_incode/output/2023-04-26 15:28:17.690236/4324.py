#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <file> [<file> ...]' % sys.argv[0])
        exit(1)
    
    for f in sys.argv[1:]:
        print('Removing words from %s' % f)
        
        lines = open(f, 'r').readlines()
        
        words = []
        for line in lines:
            line = line.strip()
            
            if line == '':
                continue
            
            words.append(line)
        
        with open(f, 'w') as f:
            for line in words:
                f.write(line)
        
        print('Done.')
        
