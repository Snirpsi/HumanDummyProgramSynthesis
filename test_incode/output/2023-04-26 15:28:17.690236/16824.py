#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1].split()
    
    for word in words:
        word = word.strip()
        
        if word == '':
            continue
        
        word = word.lower()
        
        if word not in STOPWORDS:
            print(word)
    
    print("Done.")
    
