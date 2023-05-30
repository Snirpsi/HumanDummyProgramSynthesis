#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port or converts a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 1
    
    words = []
    
    for word in sys.argv[2:]:
        words.append(word)
    
    words.sort()
    
    word_to_number = {}
    
    for word in words:
        word_to_number[word] = port
        port += 1
    
    word_to_number.