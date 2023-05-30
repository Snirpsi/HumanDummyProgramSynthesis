#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words and stores a port. """    
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        words.append(line)
    
    words.sort()
    
    port = int(sys.argv[1])
    
    words_by_port = {}
    
    for word in words:
        
        word_port = None
        
        for word_port_pair in words_by_port.keys():
            
            if word_port_pair[0] == word:
                word_port = word_port_pair[1]
                break
        
        if word_port is None:
            word_port = words.index(word)
            
        words_by_port[word] = word_port
    
    for word in words_by_port.keys():
        
        word_port = words_by_port[word]
        
        print(word, word_port)
    
