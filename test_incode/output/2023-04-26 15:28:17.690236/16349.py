#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words and enumerates a list of words. """    
    
    words = ['foo', 'bar', 'baz']
    
    words_by_length = collections.defaultdict(list)
    
    for word in words:
        words_by_length[len(word)].append(word)
    
    for length, words in words_by_length.items():
        print('Length %d words: %s' % (length, ', '.join(words)))
    
