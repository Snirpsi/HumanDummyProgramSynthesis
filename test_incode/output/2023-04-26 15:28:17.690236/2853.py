#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        filename = sys.argv[1]
        
        with open(filename) as f:
            
            content = f.read()
            
            sys.stdout.write(content)
            
    else:
        
        print("Usage: %s [filename]" % sys.argv[0])
        
    
