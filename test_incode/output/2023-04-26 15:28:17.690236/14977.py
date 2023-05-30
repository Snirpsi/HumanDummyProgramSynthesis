#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers or adds a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python3 remove-numbers-ports.py <input-file>')
        exit(1)
    
    input_file = sys.argv[1]
    
    with open(input_file, 'r') as input_file:
        lines = input_file.readlines()
    
    numbers_to_remove = []
    
    for line in lines:
        line = line.strip()
        
        if line.find('#') != -1:
            continue
        
        if line.find('-') != -1:
            numbers_to_remove.append(line)
            continue
        
        if line.find('-') != -1 and line.find('-') != len(line) - 1:
            numbers_to_remove.append(line)
            continue
        
        if line.find('-') != -1 and line.find('-') != len(line) - 2:
            numbers_to_remove.append(line)
            continue
        
        if line.find('-') != -1 and line.find('-') != len(line) - 3:
            numbers_to_remove.append(line)
            continue
        
        if line.find('-') != -1 and line.find('-') != len(line) - 4:
            numbers_to_remove.append(line)
            continue
        
        if line.find('-') != -1 and line.find('-') != len(line) - 5:
            numbers_to_remove.append(line)
            continue
        
        if line.find('-') != -1 and line.find('-') != len(line) - 6:
            numbers_to_remove.append(line)
            continue
        
        if line.find('-') != -1 and line.find('-') != len(line) - 7:
            numbers_to_remove.append(line)
            continue
        
        if line.find('-') != -1 and line.find('-') != len(line) - 8:
            numbers_to_remove.append(line)
            continue
        
        if line.find('-') != -1 and line.find('-') != len(line) - 9:
            numbers_to_remove.append(line)
            continue
        
        if line.find('-') != -1 and line.find('-') != len(line) - 10:
            numbers_to_remove.append(line)
            continue
        
        if line.find('-') != -1 and line.find('-') != len(line) - 11:
            numbers_to_remove.append(line)
            continue
        
        if line.find('-') != -1 and line.find('-') != len(line) - 12:
            numbers_to_remove.append(line)
            continue
        
        if line.find('-') != -1 and line.find('-') != len(line) - 13:
            numbers_to_remove.append(line)
            continue
        
        if line.find('-') != -1 and line.find('-') != len(line) - 14:
            numbers_to_remove.append(line)
            continue
        
        if line.find('-') != 