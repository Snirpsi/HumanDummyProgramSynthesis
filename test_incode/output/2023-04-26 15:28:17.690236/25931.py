#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or removes words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove-words-from-numbers-or-remove-words-from-a-file.py")
        exit(1)
    
    file = sys.argv[1]
    
    if file.endswith(".txt"):
        file = open(file, "r")
    
    lines = file.readlines()
    
    words = []
    
    for line in lines:
        line = line.strip()
        
        if line.startswith("#"):
            continue
        
        if line.startswith("-"):
            words.append(line)
            continue
        
        if line.startswith("+"):
            words.append(line[1:])
            continue
        
        if line.startswith("-"):
            words.append(line[1:])
            continue
        
        if line.startswith("+"):
            words.append(line[1:])
            continue
        
        if line.startswith("-"):
            words.append(line[1:])
            continue
        
        if line.startswith("+"):
            words.append(line[1:])
            continue
        
        if line.startswith("-"):
            words.append(line[1:])
            continue
        
        if line.startswith("+"):
            words.append(line[1:])
            continue
        
        if line.startswith("-"):
            words.append(line[1:])
            continue
        
        if line.startswith("+"):
            words.append(line[1:])
            continue
        
        if line.startswith("-"):
            words.append(line[1:])
            continue
        
        if line.startswith("+"):
            words.append(line[1:])
            continue
        
        if line.startswith("-"):
            words.append(line[1:])
            continue
        
        if line.startswith("+"):
            words.append(line[1:])
            continue
        
        if line.startswith("-"):
            words.append(line[1:])
            continue
        
        if line.startswith("+"):
            words.append(line[1:])
            continue
        
        if line.startswith("-"):
            words.append(line[1:])
            continue
        
        if line.startswith("+"):
            words.append(line[1:])
            continue
        
        if line.startswith("-"):
            words.append(line[1:])
            continue
        
        if line.startswith("+"):
            words.append(line[1:])
            continue
        
        if line.startswith("-"):
            words.append(line[1:])
            continue
        
        if line.startswith("+"):
            words.append(line[1:])
            continue
        
        if line.startswith("-"):
            words.append(line[1:])
            continue
        
        if line.startswith("+"):
            words.append(line[1:])
            continue
        
        if line.startswith("-"):
            words.append(line[1:])
            continue
        
        if line.startswith("+"):
            words.append(line[1:])
            continue
        
        if line.