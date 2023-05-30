#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words or removes a port. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
    
    words = list(set(words))
    
    words.sort()
    
    for word in words:
        print(word)
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word in words:
            words.remove(word)
            
            for word in words:
                print(word)
        else:
            print("No such word.")
    else:
        print("No words given.")
    
