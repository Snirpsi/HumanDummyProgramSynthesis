#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        for line in sys.stdin:
            line = line.strip()
            if line == '':
                continue
            words.append(line)
        
        words.sort()
        
        print('\n'.join(words))
    else:
        print('Usage: %s <words>' % sys.argv[0])
    
