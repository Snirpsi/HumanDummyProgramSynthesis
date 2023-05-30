#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <word>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.strip()
        
        if word == "":
            continue
        
        sys.stdout.write(word)
        sys.stdout.write("\n")
    
    sys.stdout.write("\n")
    
