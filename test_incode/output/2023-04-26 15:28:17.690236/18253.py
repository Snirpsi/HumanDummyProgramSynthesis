#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
        with open(filename) as file:
            content = file.read()
            
        sys.stdout.write(content)
    else:
        print('Usage: %s <filename>' % sys.argv[0])
        
