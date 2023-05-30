#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words and calculates a port. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == "":
            continue
        
        words.append(line)
        
    words.sort()
    
    port = 0
    
    for word in words:
        
        word_len = len(word)
        
        if word_len < 2:
            continue
        
        word_1 = word[0:word_len - 1]
        word_2 = word[word_len - 1]
        
        word_1 = word_1.lower()
        word_2 = word_2.lower()
        
        if word_1 == word_2:
            
            port += 1
        
    print(port)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    