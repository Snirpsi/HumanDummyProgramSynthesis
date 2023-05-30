#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers or prints a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <file> [<file> ...]" % sys.argv[0])
        sys.exit()
    
    for filename in sys.argv[1:]:
        
        with open(filename) as file:
            
            for line in file:
                
                line = line.strip()
                
                if line.isdigit():
                    
                    sys.stdout.write(line)
                    
                elif line.isalpha():
                    
                    sys.stdout.write(line)
                    
                else:
                    
                    sys.stdout.write('\n')
                    
    
