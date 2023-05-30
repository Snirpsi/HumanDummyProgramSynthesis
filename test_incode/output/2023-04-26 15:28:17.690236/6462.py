#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s word1 word2 word3 ...' % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in sys.argv[1:]]
    
    for word in words:
        word = word.lower()
        
        if word not in words:
            print('%s is not in the list' % word)
    
    print('Done')
    
