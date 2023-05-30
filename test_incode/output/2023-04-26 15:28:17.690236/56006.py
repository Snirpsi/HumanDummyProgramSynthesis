#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds user input or converts words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 words.py")
        exit()
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.strip()
        
        if len(word) == 0:
            continue
        
        if word.startswith('-'):
            word = word[1:]
            
        if word.startswith('+'):
            word = word[1:]
            
        if word.startswith('*'):
            word = word[1:]
            
        if word.startswith('?'):
            word = word[1:]
            
        if word.startswith('!'):
            word = word[1:]
            
        if word.startswith('@'):
            word = word[1:]
            
        if word.startswith('#'):
            word = word[1:]
            
        if word.startswith('$'):
            word = word[1:]
            
        if word.startswith('%'):
            word = word[1:]
            
        if word.startswith('^'):
            word = word[1:]
            
        if word.startswith('&'):
            word = word[1:]
            
        if word.startswith('*'):
            word = word[1:]
            
        if word.startswith('('):
            word = word[1:]
            
        if word.endswith(')'):
            word = word[:-1]
            
        if word.startswith('['):
            word = word[1:]
            
        if word.endswith(']'):
            word = word[:-1]
            
        if word.startswith('{'):
            word = word[1:]
            
        if word.endswith('}'):
            word = word[:-1]
            
        if word.startswith('<'):
            word = word[1:]
            
        if word.endswith('>'):
            word = word[:-1]
            
        if word.startswith('='):
            word = word[1:]
            
        if word.endswith('='):
            word = word[:-1]
            
        if word.startswith('>='):
            word = word[1:]
            
        if word.endswith('>='):
            word = word[:-1]
            
        if word.startswith('<='):
            word = word[1:]
            
        if word.endswith('<='):
            word = word[:-1]
            
        if word.startswith('!='):
            word = word[1:]
            
        if word.endswith('!='):
            word = word[:-1]
            
        if word.startswith('=='):
            word = word[1:]
            
        if word.endswith('=='):
            word = word[:-1]
            
        if word.startswith('!='):
            word = word[1:]
            
        if word.endswith('!='):
            word = word[:-1]
            
        if word.startswith('<'):
            word = word[1:]
            
        if word.endswith('<'):
            word = word[:-1]
            
        if word.startswith('>'):
            word = word[1:]
