#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words and removes words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.strip()
        
        if word:
            sys.stdout.write(word + "\n")
        else:
            sys.stdout.write("\n")
    
    sys.stdout.write("\n")
    
