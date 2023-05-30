#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words and removes a port. """    
    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.strip()
        
        if word:
            word = word.lower()
            
            if word[0] == '#':
                word = word[1:]
                
            if word[0] == '-':
                word = word[1:]
                
            if word[0] == '.':
                word = word[1:]
                
            if word[0] == '?':
                word = word[1:]
                
            if word[0] == '!':
                word = word[1:]
                
            if word[0] == '$':
                word = word[1:]
                
            if word[0] == '&':
                word = word[1:]
                
            if word[0] == '*':
                word = word[1:]
                
            if word[0] == '(':
                word = word[1:]
                
            if word[0] == ')':
                word = word[1:]
                
            if word[0] == '[':
                word = word[1:]
                
            if word[0] == ']':
                word = word[1:]
                
            if word[0] == '{':
                word = word[1:]
                
            if word[0] == '}':
                word = word[1:]
                
            if word[0] == '^':
                word = word[1:]
                
            if word[0] == '|':
                word = word[1:]
                
            if word[0] == '~':
                word = word[1:]
                
            if word[0] == '<':
                word = word[1:]
                
            if word[0] == '>':
                word = word[1:]
                
            if word[0] == '?':
                word = word[1:]
                
            if word[0] == '!':
                word = word[1:]
                
            if word[0] == '$':
                word = word[1:]
                
            if word[0] == '&':
                word = word[1:]
                
            if word[0] == '*':
                word = word[1:]
                
            if word[0] == '(':
                word = word[1:]
                
            if word[0] == ')':
                word = word[1:]
                
            if word[0] == '[':
                word = word[1:]
                
            if word[0] == ']':
                word = word[1:]
                
            if word[0] == '{':
                word = word[1:]
                
            if word[0] == '}':
                word = word[1:]
                
            if word[0] == '^':
                word = word[1:]
                
            if word[0] == '|':
                word = word[1:]
                
            if word[0] == '~':
                word = word[1:]
                
            if word[0] == '<':
                word = word[1:]
                
            if word[0] == '>':
                word = word[1:]
                
            if word[0] == '?':
                word = word[1:]
                
            if word[0] == '!':
                word = word