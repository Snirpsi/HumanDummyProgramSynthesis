#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words or enumerates a list of words. """    
    words = sys.argv[1:]
    
    if len(words) == 0:
        print('Usage: %s [words...]' % sys.argv[0])
        sys.exit()
    
    words = list(set(words))
    
    if len(words) == 1:
        print('%s: %s' % (sys.argv[0], words[0]))
    else:
        print('%s: %s' % (sys.argv[0], ', '.join(words)))
    
    for word in words:
        print('%s: %s' % (word, word_to_