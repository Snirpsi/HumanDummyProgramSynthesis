#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and converts words. """    
    
    words = []
    
    words.append("word1")
    words.append("word2")
    words.append("word3")
    
    words.sort()
    
    for word in words:
        print(word)
        
