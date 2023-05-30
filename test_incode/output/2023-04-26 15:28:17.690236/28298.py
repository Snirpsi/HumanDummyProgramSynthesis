#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of words or converts all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'add':
            
            words = sys.argv[2:]
            
            addWords(words)
            
        elif sys.argv[1] == 'convert':
            
            words = sys.argv[2:]
            
            convertWords(words)
            
        else:
            
            print('Usage: %s add <words>' % sys.argv[0])
            
    else:
        
        print('Usage: %s add <words>' % sys.argv[0])
        
