#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <file> [<file> ...]" % sys.argv[0])
        sys.exit()
    
    for f in sys.argv[1:]:
        lines = open(f).readlines()
        
        for line in lines:
            line = line.strip()
            
            if line.isdigit():
                sys.stdout.write(line)
                
            else:
                sys.stdout.write(line.replace('\n', ' '))
                
            sys.stdout.write('\n')
            
        sys.stdout.write('\n')
        
    