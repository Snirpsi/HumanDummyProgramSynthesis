#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or multiplyes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word1 = sys.argv[1]
        word2 = sys.argv[2]
        
        if word1 == 'add':
            word1 = word1 + word2
        elif word1 == 'multiply':
            word1 = word1 * word2
        else:
            print('Usage: %s add <word1> <word2>' % sys.argv[0])
            sys.exit(1)
        
        print('%s + %s = %s' % (word1, word2, word1))
    else:
        print('Usage: %s add <word1> <word2>' % sys.argv[0])
        sys.exit(1)
    
    print('Server running at http://127.0.0.1:8000/' % sys.argv[0])
    
