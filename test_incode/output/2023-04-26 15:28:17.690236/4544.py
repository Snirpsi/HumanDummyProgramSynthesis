#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and enumerates a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        for arg in sys.argv[1:]:
            words.append(arg)
    else:
        words = sys.argv[1:]
    
    words.sort()
    
    wordpairs = zip(words, range(1, len(words) + 1))
    
    wordpairs.sort(key=lambda x: x[0])
    
    wordpairs.reverse()
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    
    wordpairs.insert(0, ('', ''))
    