#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        for line in sys.stdin:
            line = line.strip()
            if line:
                words.append(line)
        
        words.sort()
        
        print(' '.join(words))
    else:
        print('Usage: {} <words>'.format(sys.argv[0]))
        
