#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a port or multiplyes words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <word1> <word2> ... <wordN>' % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in sys.argv[1:]]
    
    for word in words:
        
        if word == '':
            continue
        
        word = ''.join(word)
        
        if word == '':
            continue
        
        word = int(word)
        
        if word < 0:
            continue
        
        words.append(word)
    
    words = list(set(words))
    
    words.sort()
    
    for word in words:
        
        if word == '':
            continue
        
        word = ''.join(word)
        
        if word == '':
            continue
        
        word = int(word)
        
        if word < 0:
            continue
        
        words.append(word)
    
    print('\n'.join(words))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
