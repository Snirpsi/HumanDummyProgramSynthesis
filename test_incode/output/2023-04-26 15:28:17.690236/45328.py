#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <file> [<file> ...]" % sys.argv[0])
        sys.exit()
    
    for filename in sys.argv[1:]:
        with open(filename) as file:
            lines = file.readlines()
            
        lines = filter(None, lines)
        
        with open(filename, 'w') as file:
            for line in lines:
                file.write(line)
                file.write('\n')
    
    print("Done.")
