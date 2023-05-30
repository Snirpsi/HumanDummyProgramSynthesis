#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.strip()
        
        if len(word) == 0:
            continue
        
        word = word.lower()
        
        if word in word_dict:
            print(word_dict[word])
        else:
            print('%s is not in word_dict' % word)
    
