#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a port or converts a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
    else:
        port = 1
    
    wordlist = sys.argv[2:]
    
    for word in wordlist:
        word = word.strip()
        
        if word == '':
            continue
        
        if word.startswith('-'):
            word = word[1:]
            
        if word.startswith('+'):
            word = word[1:]
            
        if word.startswith('#'):
            word = word[1:]
            
        if word.startswith('@'):
            word = word[1:]
            
        if word.startswith('.'):
            word = word[1:]
            
        if word.startswith('['):
            word = word[1:]
            
        if word.startswith(']'):
            word = word[1:]
            
        if word.startswith('?'):
            word = word[1:]
            
        if word.startswith('!'):
            word = word[1:]
            
        if word.startswith(':'):
            word = word[1:]
            
        if word.startswith('<'):
            word = word[1:]
            
        if word.startswith('>'):
            word = word[1:]
            
        if word.startswith('"'):
            word = word[1:]
            
        if word.startswith('\''):
            word = word[1:]
            
        if word.startswith('|'):
            word = word[1:]
            
        if word.startswith('>'):
            word = word[1:]
            
        if word.startswith('<'):
            word = word[1:]
            
        if word.startswith('!'):
            word = word[1:]
            
        if word.startswith(':'):
            word = word[1:]
            
        if word.startswith('@'):
            word = word[1:]
            
        if word.startswith('.'):
            word = word[1:]
            
        if word.startswith('['):
            word = word[1:]
            
        if word.startswith(']'):
            word = word[1:]
            
        if word.startswith('?'):
            word = word[1:]
            
        if word.startswith('!'):
            word = word[1:]
            
        if word.startswith(':'):
            word = word[1:]
            
        if word.startswith('<'):
            word = word[1:]
            
        if word.startswith('>'):
            word = word[1:]
            
        if word.startswith('"'):
            word = word[1:]
            
        if word.startswith('\''):
            word = word[1:]
            
        if word.startswith('|'):
            word = word[1:]
            
        if word.startswith('>'):
            word = word[1:]
            
        if word.startswith('<'):
            word = word[1:]
            
        if word.startswith('!'):
            word = word[1:]
            
        if word.startswith(':'):
            word = word[1:]
            
        if 