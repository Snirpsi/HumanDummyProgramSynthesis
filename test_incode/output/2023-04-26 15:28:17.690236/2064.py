#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words and calculates all ports. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        words = line.split()
        
        if len(words) != 2:
            continue
        
        words.append(words[0])
        words.append(words[1])
        
        words.sort()
        
        ports = []
        
        for word in words:
            
            word = word.strip()
            
            if word:
                
                ports.append(word)
                
                word = word.lower()
                
                if word[0].isdigit():
                    
                    word = word[1:]
                    
                    ports.append(word)
                    
                else:
                    
                    word = word[0]
                    
                    ports.append(word)
                    
                    word = word[1:]
                    
                    ports.append(word)
                    
                    word = word[0]
                    
                    ports.append(word)
                    
                    word = word[1:]
                    
                    ports.append(word)
                    
                    word = word[0]
                    
                    ports.append(word)
                    
                    word = word[1:]
                    
                    ports.append(word)
                    
                    word = word[0]
                    
                    ports.append(word)
                    
                    word = word[1:]
                    
                    ports.append(word)
                    
                    word = word[0]
                    
                    ports.append(word)
                    
                    word = word[1:]
                    
                    ports.append(word)
                    
                    word = word[0]
                    
                    ports.append(word)
                    
                    word = word[1:]
                    
                    ports.append(word)
                    
                    word = word[0]
                    
                    ports.append(word)
                    
                    word = word[1:]
                    
                    ports.append(word)
                    
                    word = word[0]
                    
                    ports.append(word)
                    
                    word = word[1:]
                    
                    ports.append(word)
                    
                    word = word[0]
                    
                    ports.append(word)
                    
                    word = word[1:]
                    
                    ports.append(word)
                    
                    word = word[0]
                    
                    ports.append(word)
                    
                    word = word[1:]
                    
                    ports.append(word)
                    
                    word = word[0]
                    
                    ports.append(word)
                    
                    word = word[1:]
                    
                    ports.append(word)
                    
                    word = word[0]
                    
                    ports.append(word)
                    
                    word = word[1:]
                    
                    ports.append(word)
                    
                    word = word[0]
                    
                    ports.append(word)
                    
                    word = word[1:]
                    
                    ports.append(word)
                    
                    word = word[0]
                    
                    ports.append(word)
                    
                    