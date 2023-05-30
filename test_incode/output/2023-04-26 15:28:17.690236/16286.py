#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words or stores a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python word.py <word>", file=sys.stderr)
        exit(1)
    
    word = sys.argv[1]
    
    word_len = len(word)
    
    word_list = list(word)
    
    word_list.insert(word_len, 'e')
    
    word_list.insert(word_len, 'a')
    
    word_list.insert(word_len, 'o')
    
    word_list.insert(word_len, 'u')
    
    word_list.insert(word_len, '