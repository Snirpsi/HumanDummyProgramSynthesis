#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        exit(1)
    
    words = sys.argv[1:]
    
    for word in words:
        words = word.split(' ')
        
        for word in words:
            word = word.strip()
            
            if word != '':
                