#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words. """    
    import sys
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    words.sort()
    
    i = 0
    
    while i < len(words):
        word = words[i]
        
        if word == '':
            i += 1
            continue
        
        if word[0] == '-':
            words[i] = word[1:]
            continue
        
        if word[-1] == '-':
            words[i] = word[:-1]
            continue
        
        i += 1
    
    i = 0
    
    while i < len(words):
        word = words[i]
        
        if word == '':
            i += 1
            continue
        
        i += 1
    
    i = 0
    
    while i < len(words):
        word = words[i]
        
        if word == '':
            i += 1
            continue
        
        i += 1
    
    i = 0
    
    while i < len(words):
        word = words[i]
        
        if word == '':
            i += 1
            continue
        
        i += 1
    
    i = 0
    
    while i < len(words):
        word = words[i]
        
        if word == '':
            i += 1
            continue
        
        i += 1
    
    i = 0
    
    while i < len(words):
        word = words[i]
        
        if word == '':
            i += 1
            continue
        
        i += 1
    
    i = 0
    
    while i < len(words):
        word = words[i]
        
        if word == '':
            i += 1
            continue
        
        i += 1
    
    i = 0
    
    while i < len(words):
        word = words[i]
        
        if word == '':
            i += 1
            continue
        
        i += 1
    
    i = 0
    
    while i < len(words):
        word = words[i]
        
        if word == '':
            i += 1
            continue
        
        i += 1
    
    i = 0
    
    while i < len(words):
        word = words[i]
        
        if word == '':
            i += 1
            continue
        
        i += 1
    
    i = 0
    
    while i < len(words):
        word = words[i]
        
        if word == '':
            i += 1
            continue
        
        i += 1
    
    i = 0
    
    while i < len(words):
        word = words[i]
        
        if word == '':
            i += 1
            continue
        
        i += 1
    
    i = 0
    
    while i < len(words):
        word = words[i]
        
        if word == '':
            i += 1
            continue
        