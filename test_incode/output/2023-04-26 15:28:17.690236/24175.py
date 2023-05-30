#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words. """    
    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        
        word = word.strip()
        
        if word == '':
            continue
        
        if word.startswith('http'):
            continue
        
        if word.startswith('https'):
            continue
        
        if word.startswith('http'):
            
            webbrowser.open(word)
        
        else:
            
            webbrowser.open(word