#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words or opens user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter a filename: ")
    
    file = open(filename, 'r')
    
    for line in file:
        line = line.strip()
        
        if line == '' or line == '\n':
            continue
        
        if line == '.':
            print(line)
            continue
        
        if line == '?':
            print(line)
            continue
        
        if line == '!':
            print(line)
            continue
        
        if line == '?!':
            print(line)
            continue
        
        if line == '!?':
            print(line)
            continue
        
        if line == '!?!':
            print(line)
            continue
        
        if line == '!?!?':
            print(line)
            continue
        
        if line == '!?!?!':
            print(line)
            continue
        
        if line == '!?!?!?':
            print(line)
            continue
        
        if line == '!?!?!?!?':
            print(line)
            continue
        
        if line == '!?!?!?!?!?':
            print(line)
            continue
        
        if line == '!?!?!?!?!?!?':
            print(line)
            continue
        
        if line == '!?!?!?!?!?!?!?':
            print(line)
            continue
        
        if line == '!?!?!?!?!?!?!?!?':
            print(line)
            continue
        
        if line == '!?!?!?!?!?!?!?!?!?':
            print(line)
            continue
        
        if line == '!?!?!?!?!?!?!?!?!?!?':
            print(line)
            continue
        
        if line == '!?!?!?!?!?!?!?!?!?!?':
            print(line)
            continue
        
        if line == '!?!?!?!?!?!?!?!?!?!?':
            print(line)
            continue
        
        if line == '!?!?!?!?!?!?!?!?!?!?!?':
            print(line)
            continue
        
        if line == '!?!?!?!?!?!?!?!?!?!?!?':
            print(line)
            continue
        
        if line == '!?!?!