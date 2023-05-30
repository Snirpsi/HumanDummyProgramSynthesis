#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    import sys
    wordlist = sys.argv[1:]
    
    for word in wordlist:
        word = word.strip()
        
        if word == '':
            continue
        
        if word.startswith('-'):
            continue
        
        if word.startswith('+'):
            word = word[1:]
            
        if word.startswith('*'):
            word = word[1:]
            
        if word.startswith('?'):
            word = word[1:]
            
        if word.startswith('!'):
            word = word[1:]
            
        if word.startswith('#'):
            word = word[1:]
            
        if word.startswith('$'):
            word = word[1:]
            
        if word.startswith('@'):
            word = word[1:]
            
        if word.startswith('%'):
            word = word[1:]
            
        if word.startswith('&'):
            word = word[1:]
            
        if word.startswith('*'):
            word = word[1:]
            
        if word.startswith('('):
            word = word[1:]
            
        if word.endswith(')'):
            word = word[:-1]
            
        if word.startswith('"'):
            word = word[1:]
            
        if word.startswith('<'):
            word = word[1:]
            
        if word.startswith('>'):
            word = word[1:]
            
        if word.startswith(':'):
            word = word[1:]
            
        if word.startswith(';'):
            word = word[1:]
            
        if word.startswith('='):
            word = word[1:]
            
        if word.startswith('>='):
            word = word[1:]
            
        if word.startswith('<='):
            word = word[1:]
            
        if word.startswith('>'):
            word = word[1:]
            
        if word.startswith('<'):
            word = word[1:]
            
        if word.startswith('>'):
            word = word[1:]
            
        if word.startswith('<'):
            word = word[1:]
            
        if word.startswith('>'):
            word = word[1:]
            
        if word.startswith('='):
            word = word[1:]
            
        if word.startswith('>='):
            word = word[1:]
            
        if word.startswith('<='):
            word = word[1:]
            
        if word.startswith('>'):
            word = word[1:]
            
        if word.startswith('<'):
            word = word[1:]
            
        if word.startswith('>'):
            word = word[1:]
            
        if word.startswith('<'):
            word = word[1:]
            
        if word.startswith('>'):
            word = word[1:]
            
        if word.startswith('<'):
            word = word[1:]
            
        if word.startswith('>'):
            word = word[1:]
            
        if word.startswith('<'):
            word = word[1:]