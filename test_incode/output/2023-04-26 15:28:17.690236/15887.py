#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(1)
    
    words = sys.argv[1:]
    
    words = words.split()
    
    words += ['']
    
    for word in words:
        word = word.strip()
        
        if word:
            print('%s %s' % (word, ' '.join(words)))
        else:
            print('')
    
