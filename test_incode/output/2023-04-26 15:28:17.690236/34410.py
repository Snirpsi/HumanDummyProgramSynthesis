#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <word1> <word2> ...' % sys.argv[0])
        sys.exit()
    
    word1 = sys.argv[1]
    word2 = sys.argv[2:]
    
    word1words = word1.split()
    word2words = word2.split()
    
    word1words.sort()
    word2words.sort()
    
    word1words = [w for w in word1words if w not in word2words]
    word2words = [w for w in word2words if w not in word1words]
    
    word1words = [w for w in word1words if len(w) > 1]
    word2words = [w for w in word2words if len(w) > 1]
    
    word1words = [w for w in word1words if len(w) == 1]
    word2words = [w for w in word2words if len(w) == 1]
    
    word1words = [w for w in word1words if w not in word2words]
    word2words = [w for w in word2words if w not in word1words]
    
    word1words = [w for w in word1words if len(w) > 1]
    word2words = [w for w in word2words if len(w) > 1]
    
    word1words = [w for w in word1words if len(w) == 1]
    word2words = [w for w in word2words if len(w) == 1]
    
    word1words = [w for w in word1words if w not in word2words]
    word2words = [w for w in word2words if w not in word1words]
    
    word1words = [w for w in word1words if len(w) > 1]
    word2words = [w for w in word2words if len(w) > 1]
    
    word1words = [w for w in word1words if len(w) == 1]
    word2words = [w for w in word2words if len(w) == 1]
    
    word1words = [w for w in word1words if w not in word2words]
    word2words = [w for w in word2words if w not in word1words]
    
    word1words = [w for w in word1words if len(w) > 1]
    word2words = [w for w in word2words if len(w) > 1]
    
    word1words = [w for w in word1words if w not in word2words]
    word2words = [w for w in word2words if w not in word1words]
    
    word1words = [w for w in word1words if len(