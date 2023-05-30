#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words and multiplyes words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.strip()
        
        if word == '':
            continue
        
        word = int(word)
        
        if word < 0:
            continue
        
        words = [word for word in words if word > 0]
        
        words = [word * -1 for word in words]
        
        print(' '.join(words))
        
