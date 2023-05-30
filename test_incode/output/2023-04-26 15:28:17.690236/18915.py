#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers or stores a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as file:
        lines = file.readlines()
        
    words = []
    
    for line in lines:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        line = line.split()
        
        if len(line) < 2:
            continue
        
        word = line[0]
        
        if word in words:
            continue
        
        words.append(word)
        
    words.sort()
    
    with open(filename, 'w') as file:
        file.write('\n'.join(words))
        
    print("Removed %d words from %s" % (len(words), filename))
    
