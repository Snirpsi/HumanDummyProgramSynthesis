#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.strip()
        
        if word == "":
            continue
        
        word = word.lower()
        
        if word == "help":
            print("Usage: %s <words>" % sys.argv[0])
            sys.exit()
        
        if word == "exit":
            sys.exit()
        
        if word == "quit":
            sys.exit()
        
        if word == "quitall":
            sys.exit()
        
        if word == "quitall