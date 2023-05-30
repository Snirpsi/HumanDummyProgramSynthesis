#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers or opens words. """    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'input.txt'
        
    with open(filename) as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        
        if line == '':
            continue
        
        if line[0] == '#':
            continue
        
        if line[0] == '*':
            print(line)
            continue
        
        if line[0] == '/':
            print(line)
            continue
        
        if line[0] == '+':
            print(line)
            continue
        
        if line[0] == '-':
            print(line)
            continue
        
        if line[0] == '=':
            print(line)
            continue
        
        if line[0] == '<':
            print(line)
            continue
        
        if line[0] == '>':
            print(line)
            continue
        
        if line[0] == '?':
            print(line)
            continue
        
        if line[0] == '!':
            print(line)
            continue
        
        if line[0] == '/':
            print(line)
            continue
        
        if line[0] == '|':
            print(line)
            continue
        
        if line[0] == '^':
            print(line)
            continue
        
        if line[0] == '~':
            print(line)
            continue
        
        if line[0] == '[':
            print(line)
            continue
        
        if line[0] == ']':
            print(line)
            continue
        
        if line[0] == '{':
            print(line)
            continue
        
        if line[0] == '}':
            print(line)
            continue
        
        if line[0] == '"':
            print(line)
            continue
        
        if line[0] == '<':
            print(line)
            continue
        
        if line[0] == '>':
            print(line)
            continue
        
        if line[0] == '|':
            print(line)
            continue
        
        if line[0] == '^':
            print(line)
            continue
        
        if line[0] == '~':
            print(line)
            continue
        
        if line[0] == '"':
            print(line)
            continue
        
        if line[0] == '"':
            print(line)
            continue
        
        if line[0] == '"':
            print(line)
            continue
        
        if line[0] == '"':
            print(line)
            continue
        
        if line[0] == '"':
            print(line)
            continue
        
        if line[0] == '"':
            print(line)
            continue
        
        if line[0] == '"':
            print(line)
            continue
        
        if line[0] == '"':
            print(line)
            continue
        
        if line[0] == '"':
            print(line)
            continue
        
        if line[0] == '"':
            print(line)
            continue
        
        if line[0] == '"':
            print(line)
            continue
        
        if line[0] == '"':
            print(line)