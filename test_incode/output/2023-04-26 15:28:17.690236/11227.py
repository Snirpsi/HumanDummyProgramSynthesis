#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter a filename: ")
    
    words = []
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    words.sort()
    
    print("\n".join(words))
    
