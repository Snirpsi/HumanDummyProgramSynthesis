#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input and opens words. """    
    
    import sys
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words = line.split(' ')
        
        for word in words:
            word = word.strip()
            
            if word == '':
                continue
            
            word = word.lower()
            
            if word not in stop_words:
                print(word)
                
