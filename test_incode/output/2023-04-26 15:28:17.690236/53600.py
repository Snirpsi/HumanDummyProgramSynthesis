#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
        with open(filename, 'r') as f:
            words = f.read().split()
            
        words = [w for w in words if w != '']
        
        with open(filename, 'w') as f:
            f.write(' '.join(words))
    else:
        print('Usage: %s <filename>' % sys.argv[0])
        
