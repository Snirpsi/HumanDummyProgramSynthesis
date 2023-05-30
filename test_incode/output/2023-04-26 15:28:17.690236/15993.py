#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers or removes words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python words_to_number.py <filename>")
        exit()
    
    filename = sys.argv[1]
    
    with open(filename) as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        if line[0].isdigit():
            print(line)
        else:
            print(line.replace(" ", ""))
    
