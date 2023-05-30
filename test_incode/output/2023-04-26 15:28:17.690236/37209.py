#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter the filename to open: ")
        
    file = open(filename, 'r')
    
    for line in file:
        line = line.strip()
        
        if line.startswith("#"):
            continue
        
        words = line.split()
        
        if len(words) > 1:
            print(" ".join(words))
        else:
            print(line)
    
    file.close()
    
