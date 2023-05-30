#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words or converts a list of words. """    
    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    words_to_remove = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    words_to_convert = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    words_to_convert = list(set(words_to_convert))
    
    words_to_remove = list(set(words_to_remove))
    
    words_to_remove.sort()
    
    words_to_convert.sort()
    
    words_to_convert.reverse()
    
    words_to_remove.reverse()
    
    words_to_remove.extend(words_to_convert)
    
    words_to_convert.extend(words_to_remove)
    
    words_to_convert = list(set(words_to_convert))
    
    words_to_convert.sort()
    
    words_to_convert = list(set(words_to_convert))
    
    words_to_convert.reverse()
    
    words_to_convert.extend(words_to_remove)
    
    words_to_convert = list(set(words_to_convert))
    
    words_to_convert.sort()
    
    words_to_convert = list(set(words_to_convert))
    
    words_to_convert.reverse()
    
    words_to_convert.extend(words_to_remove)
    
    words_to_convert = list(set(words_to_convert))
    
    words_to_convert.sort()
    
    words_to_convert = list(set(words_to_convert))
    
    words_to_convert.reverse()
    
    words_to_convert.extend(words_to_remove)
    
    words_to_convert = list(set(words_to_convert))
    
    words_to_convert.sort()
    
    words_to_convert = list(set(words_to_convert))
    
    words_to_convert.reverse()
    
    words_to_convert.extend(words_to_remove)
    
    words_to_convert = list(set(words_to_convert))
    
    words_to_convert.sort()
    
    words_to_convert = list(set(words_to_convert))
    
    words_to_convert.reverse()
    
    words_to_convert.extend(words_to_remove)
    
    words_to_convert = list(set(words_to_convert))
    