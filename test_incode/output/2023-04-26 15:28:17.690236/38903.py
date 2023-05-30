#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words and removes a port. """    
    import sys
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words.sort()
    
    i = 0
    while i < len(words):
        word = words[i]
        
        if word == '':
            i += 1
            continue
        
        if word[0] == '-':
            i += 1
            continue
        
        if word[0] == '+':
            word = word[1:]
            
        if word[0] == '#':
            word = word[1:]
            
        if word[0] == '.':
            word = word[1:]
            
        if word[0] == '-':
            word = word[1:]
            
        if word[0] == '+':
            word = word[1:]
            
        if word[0] == '#':
            word = word[1:]
            
        if word[0] == '.':
            word = word[1:]
            
        if word[0] == '-':
            word = word[1:]
            
        if word[0] == '+':
            word = word[1:]
            
        if word[0] == '#':
            word = word[1:]
            
        if word[0] == '.':
            word = word[1:]
            
        if word[0] == '-':
            word = word[1:]
            
        if word[0] == '+':
            word = word[1:]
            
        if word[0] == '#':
            word = word[1:]
            
        if word[0] == '.':
            word = word[1:]
            
        if word[0] == '-':
            word = word[1:]
            
        if word[0] == '+':
            word = word[1:]
            
        if word[0] == '#':
            word = word[1:]
            
        if word[0] == '.':
            word = word[1:]
            
        if word[0] == '-':
            word = word[1:]
            
        if word[0] == '+':
            word = word[1:]
            
        if word[0] == '#':
            word = word[1:]
            
        if word[0] == '.':
            word = word[1:]
            
        if word[0] == '-':
            word = word[1:]
            
        if word[0] == '+':
            word = word[1:]
            
        if word[0] == '#':
            word = word[1:]
            
        if word[0] == '.':
            word = word[1:]
            
        if word[0] == '-':
            word = word[1:]
            
        if word[0] == '+':
            word = word[1:]
            
        if word[0] == '#':
            word = word[1:]
            
        if word[0] == '.':
            word = word[1:]
            
        if word[0] == '-':
            word = word[1:]
            
        if word[0] == '+':
            word = word[1:]
            
        if word[0] == '#':
            word = word[1:]
            
        if word