#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words or opens numbers. """    
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        if line[0] == '#':
            continue
        
        if line[0] == '+':
            words.append(line[1:])
            continue
        
        if line[0] == '-':
            words.append(line[1:])
            continue
        
        if line[0] == '/':
            words.append(line[1:])
            continue
        
        if line[0] == '*':
            words.append(line[1:])
            continue
        
        if line[0] == '(':
            words.append(line[1:])
            continue
        
        if line[0] == ')':
            words.append(line[1:])
            continue
        
        if line[0] == '<':
            words.append(line[1:])
            continue
        
        if line[0] == '>':
            words.append(line[1:])
            continue
        
        if line[0] == '|':
            words.append(line[1:])
            continue
        
        if line[0] == '?':
            words.append(line[1:])
            continue
        
        if line[0] == '!':
            words.append(line[1:])
            continue
        
        if line[0] == '@':
            words.append(line[1:])
            continue
        
        if line[0] == '#':
            continue
        
        if line[0] == '$':
            continue
        
        if line[0] == '%':
            continue
        
        if line[0] == '^':
            continue
        
        if line[0] == '&':
            continue
        
        if line[0] == '*':
            continue
        
        if line[0] == '/':
            continue
        
        if line[0] == '+':
            continue
        
        if line[0] == '-':
            continue
        
        if line[0] == '(':
            continue
        
        if line[0] == ')':
            continue
        
        if line[0] == '|':
            continue
        
        if line[0] == '?':
            continue
        
        if line[0] == '!':
            continue
        
        if line[0] == '@':
            continue
        
        if line[0] == '#':
            continue
        
        if line[0] == '$':
            continue
        
        if line[0] == '%':
            continue
        
        if line[0] == '^':
            continue
        
        if line[0] == '&':
            continue
        
        if line[0] == '*':
            continue
        
        if line[0] == '/':
            continue
        
        if line[0] == '+':
            continue
        
        if line[0] == '-':
            continue
        
        if line[0] == '(':
            continue
        
        if line[0] == ')':
            continue
        
        if line[0] == '|':
            continue
        
        if line[0] == '?':
            continue
        
        if line[0] == '!':