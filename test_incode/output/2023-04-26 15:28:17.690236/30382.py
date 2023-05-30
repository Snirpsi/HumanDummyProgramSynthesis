#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or enumerates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python enumerate.py <file> [<file> ...]")
        sys.exit()
    
    file = sys.argv[1]
    
    for filename in sys.argv[2:]:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if line:
                    sys.stdout.write(line)
                else:
                    sys.stdout.write('\n')
