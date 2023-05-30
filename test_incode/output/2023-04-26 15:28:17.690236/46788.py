#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(1)
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.strip()
        
        if word == '':
            continue
        
        if word[0].isupper():
            word = word.upper()
        
        if word[0].islower():
            word = word.lower()
        
        if word[0].isdigit():
            word = word[0]
        
        if word[0].isalpha():
            word = word[0]
        
        if word[0].isspace():
            continue
        
        if word[0].isdigit():
            word = word[1:]
        
        if word[0].isalpha():
            word = word[1:]
        
        if word[0].isspace():
            continue
        
        if word[0].isdigit():
            word = word[1:]
        
        if word[0].isalpha():
            word = word[1:]
        
        if word[0].isspace():
            continue
        
        if word[0].isdigit():
            word = word[1:]
        
        if word[0].isalpha():
            word = word[1:]
        
        if word[0].isspace():
            continue
        
        if word[0].isdigit():
            word = word[1:]
        
        if word[0].isalpha():
            word = word[1:]
        
        if word[0].isspace():
            continue
        
        if word[0].isdigit():
            word = word[1:]
        
        if word[0].isalpha():
            word = word[1:]
        
        if word[0].isspace():
            continue
        
        if word[0].isdigit():
            word = word[1:]
        
        if word[0].isalpha():
            word = word[1:]
        
        if word[0].isspace():
            continue
        
        if word[0].isdigit():
            word = word[1:]
        
        if word[0].isalpha():
            word = word[1:]
        
        if word[0].isspace():
            continue
        
        if word[0].isdigit():
            word = word[1:]
        
        if word[0].isalpha():
            word = word[1:]
        
        if word[0].isspace():
            continue
        
        if word[0].isdigit():
            word = word[1:]
        
        if word[0].isalpha():
            word = word[1:]
        
        if word[0].isspace():
            continue
        
        if word[0].isdigit():
            word = word[1:]
        
        if word[0].isalpha():
            word = word[1:]
        
        if word[0].isspace():
            continue
        
        if word[0]